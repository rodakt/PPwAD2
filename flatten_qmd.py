from __future__ import annotations

import argparse
import re
from pathlib import Path


# {{< include path >}} albo {{< include "path with spaces.py" >}}
INCLUDE_RE = re.compile(
    r"{{<\s*include\s+(?P<path>\"[^\"]+\"|'[^']+'|[^>]+?)\s*>}}"
)

# Linia opcji Quarto: #| file: path.py
FILE_OPTION_RE = re.compile(
    r"^(?P<indent>\s*#\|\s*file:\s*)(?P<path>.+?)\s*$"
)

# Początek fenced block
FENCE_START_RE = re.compile(
    r"^(?P<indent>\s*)(?P<fence>`{3,}|~{3,})(?P<rest>[^\n]*)\n?$"
)

# Chunk Quarto typu ```{python}
PYTHON_CHUNK_OPEN_RE = re.compile(
    r"^\s*(`{3,}|~{3,})\{python\b.*\}\s*$"
)

# Zwykły fenced block markdown typu ```python
PLAIN_PYTHON_FENCE_OPEN_RE = re.compile(
    r"^\s*(`{3,}|~{3,})\s*python\s*$"
)

# Ciało bloku zawiera wyłącznie include
INCLUDE_ONLY_RE = re.compile(
    r"^\s*{{<\s*include\s+(?P<path>\"[^\"]+\"|'[^']+'|[^>]+?)\s*>}}\s*$",
    re.DOTALL,
)


def strip_optional_quotes(text: str) -> str:
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        return text[1:-1]
    return text


def resolve_path(raw_path: str, base_file: Path) -> Path:
    path = Path(strip_optional_quotes(raw_path))
    if not path.is_absolute():
        path = base_file.parent / path
    return path.resolve()


def is_fence_start(line: str) -> tuple[str, int] | None:
    m = FENCE_START_RE.match(line)
    if not m:
        return None
    fence = m.group("fence")
    return fence[0], len(fence)


def is_fence_close(line: str, fence_char: str, min_len: int) -> bool:
    stripped = line.strip()
    return (
        len(stripped) >= min_len
        and all(ch == fence_char for ch in stripped)
    )


def replace_includes_in_text(text: str, current_file: Path, stack: tuple[Path, ...]) -> str:
    def repl(match: re.Match[str]) -> str:
        included_path = resolve_path(match.group("path"), current_file)
        return flatten_file(included_path, stack)

    return INCLUDE_RE.sub(repl, text)


def process_code_block(block_lines: list[str], current_file: Path) -> list[str]:
    if len(block_lines) < 2:
        return block_lines

    open_line = block_lines[0]
    close_line = block_lines[-1]
    body_lines = block_lines[1:-1]
    body_text = "".join(body_lines)

    # Przypadek 1:
    # ```python
    # {{< include path.py >}}
    # ```
    if PLAIN_PYTHON_FENCE_OPEN_RE.match(open_line.strip()):
        m = INCLUDE_ONLY_RE.match(body_text)
        if m is None:
            return block_lines

        included_path = resolve_path(m.group("path"), current_file)
        if not included_path.exists():
            raise FileNotFoundError(
                f"Nie znaleziono pliku wskazanego przez include: {included_path}"
            )

        included_code = included_path.read_text(encoding="utf-8")
        if included_code and not included_code.endswith("\n"):
            included_code += "\n"

        return [open_line, included_code, close_line]

    # Przypadek 2:
    # ```{python}
    # #| file: path.py
    # ...
    # ```
    if not PYTHON_CHUNK_OPEN_RE.match(open_line.strip()):
        return block_lines

    file_path: Path | None = None
    kept_body: list[str] = []

    for line in body_lines:
        m = FILE_OPTION_RE.match(line.rstrip("\n"))
        if m is not None and file_path is None:
            file_path = resolve_path(m.group("path"), current_file)
            continue
        kept_body.append(line)

    if file_path is None:
        return block_lines

    if not file_path.exists():
        raise FileNotFoundError(
            f"Nie znaleziono pliku wskazanego przez #| file: {file_path}"
        )

    injected_code = file_path.read_text(encoding="utf-8")

    out: list[str] = [open_line]
    out.extend(kept_body)

    if out and not out[-1].endswith("\n"):
        out[-1] += "\n"

    if injected_code:
        out.append(injected_code)
        if not injected_code.endswith("\n"):
            out.append("\n")

    out.append(close_line)
    return out


def flatten_file(current_file: Path, stack: tuple[Path, ...] = ()) -> str:
    current_file = current_file.resolve()

    if current_file in stack:
        cycle = " -> ".join(str(p) for p in (*stack, current_file))
        raise ValueError(f"Wykryto cykl include: {cycle}")

    if not current_file.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku: {current_file}")

    text = current_file.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    output: list[str] = []
    i = 0
    new_stack = (*stack, current_file)

    while i < len(lines):
        line = lines[i]
        fence_info = is_fence_start(line)

        if fence_info is None:
            output.append(replace_includes_in_text(line, current_file, new_stack))
            i += 1
            continue

        fence_char, fence_len = fence_info
        block = [line]
        i += 1

        while i < len(lines):
            block.append(lines[i])
            if is_fence_close(lines[i], fence_char, fence_len):
                i += 1
                break
            i += 1

        processed_block = process_code_block(block, current_file)
        output.extend(processed_block)

    return "".join(output)


def flatten_quarto_file(input_qmd: str | Path, output_qmd: str | Path) -> None:
    input_path = Path(input_qmd).resolve()
    output_path = Path(output_qmd).resolve()

    print(f"Przetwarzanie: {input_path}")
    flattened = flatten_file(input_path)
    output_path.write_text(flattened, encoding="utf-8")
    print(f"Zapisano: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Spłaszcza plik Quarto .qmd: rozwija shortcode include oraz "
            "wstawia kod z #| file: ... i z bloków ```python zawierających samo include."
        )
    )
    parser.add_argument(
        "input_qmd",
        nargs="?",
        default="v.qmd",
        help="Ścieżka do pliku wejściowego .qmd (domyślnie: v.qmd)",
    )
    parser.add_argument(
        "output_qmd",
        nargs="?",
        default="v_standalone.qmd",
        help="Ścieżka do pliku wyjściowego .qmd (domyślnie: v_standalone.qmd)",
    )
    args = parser.parse_args()

    try:
        flatten_quarto_file(args.input_qmd, args.output_qmd)
    except Exception as e:
        print(f"Błąd: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()