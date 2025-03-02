# src/triangle_area_tests_example/assert_test_triangle_area.py
from triangle_area import is_triangle, triangle_area
from math import sqrt, isclose


def test_is_triangle():
    assert is_triangle(3, 4, 5), "3, 4, 5 jest trójkątem prostokątnym"
    assert is_triangle(1, 1, 1), "Trójkąt równoboczny"
    assert is_triangle(5, 2, 3), "5, 2, 3 jest trójkątem zdegenerowanym"
    assert is_triangle(
        100, 100, sqrt(2) * 100
    ), "100, 100, 100√2 jest trójkątem prostokątnym"
    assert not is_triangle(1, 1, 3), "1, 1, 3 nie jest trójkątem"
    assert not is_triangle(-5, 2, 3), "-5, 2, 3 nie jest trójkątem"
    assert not is_triangle(1, -1, -3), "1, -1, -3 nie jest trójkątem"


def test_triangle_area():
    assert isclose(triangle_area(3, 4, 5), 6), "Pole trójkąta 3, 4, 5"
    assert isclose(triangle_area(1, 1, 1), sqrt(3) / 4), "Pole trójkąta 1, 1, 1"
    assert isclose(triangle_area(5, 2, 3), 0), "Pole trójkąta 5, 2, 3"
    assert isclose(
        triangle_area(100, 100, sqrt(2) * 100), 5000
    ), "Pole trójkąta 100, 100, 100√2"


def test_triangle_area_exceptions():
    try:
        triangle_area(1, 1, 3)
    except ValueError as e:
        assert str(e) == "Nie można zbudować trójkąta o bokach 1, 1, 3"
    else:
        raise AssertionError("Nie zgłoszono wyjątku dla 1, 1, 3")

    try:
        triangle_area(-5, 2, 3)
    except ValueError as e:
        assert str(e) == "Nie można zbudować trójkąta o bokach -5, 2, 3"
    else:
        raise AssertionError("Nie zgłoszono wyjątku dla -5, 2, 3")


def test_all():
    """Uruchamia wszystkie testy"""
    test_is_triangle()
    test_triangle_area()
    test_triangle_area_exceptions()
    print("=== All tests passed. ===")


if __name__ == "__main__":
    test_all()
