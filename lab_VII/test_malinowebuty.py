import unittest
from malinowebuty import create_key, create_encryptor


ENCRYPTED_DEFAULT = {
    "a": "m",
    "m": "a",
    "x": "x",
    "A": "A",
    "malinowebuty": "amilonewubyt",
    "ziemia jest płaska": "zlwalm jwsy płmskm",
}

KEY_PUBLIC_PRIVATE = [
    ("ab", "abc", "bac"),
    ("XYUV", "xVyU", "xUyV"),
    ("gaderypoluki", "gaderypoluki", "agedyropulik"),
]


class TestMalinowebuty(unittest.TestCase):
    """Testy jednostkowe dla funkcji z modułu malinowebuty."""

    def test_create_key_valid(self):
        """Test prawidłowego klucza."""
        with self.subTest(key="abcd"):
            self.assertEqual(create_key("abcd"), dict(a="b", b="a", c="d", d="c"))
        with self.subTest(key="malinowebuty"):
            self.assertEqual(
                create_key("malinowebuty"),
                dict(
                    m="a",
                    a="m",
                    l="i",
                    i="l",
                    n="o",
                    o="n",
                    w="e",
                    e="w",
                    b="u",
                    u="b",
                    t="y",
                    y="t",
                ),
            )

    def test_create_key_invalid(self):
        """Test nieprawidłowego klucza."""
        invalid_keys = ["", "x", "xyz", "xyzx"]
        for key in invalid_keys:
            with self.subTest(key=key):
                with self.assertRaises(ValueError) as cm:
                    create_key(key)
                self.assertEqual(str(cm.exception), "nieprawidłowy klucz.")

    def test_create_encryptor_default_key(self):
        """Test szyfrowania domyślnym kluczem."""
        for text, encrypted_text in ENCRYPTED_DEFAULT.items():
            with self.subTest(text=text, encrypted_text=encrypted_text):
                encryptor = create_encryptor()
                self.assertEqual(encryptor(text), encrypted_text)
                self.assertEqual(encryptor(encrypted_text), text)

    def test_create_encryptor_custom_key(self):
        """Test szyfrowania własnym kluczem."""
        for key, text, encrypted_text in KEY_PUBLIC_PRIVATE:
            with self.subTest(key=key, text=text, encrypted_text=encrypted_text):
                encryptor = create_encryptor(key)
                self.assertEqual(encryptor(text), encrypted_text)
                self.assertEqual(encryptor(encrypted_text), text)


if __name__ == "__main__":
    unittest.main()
