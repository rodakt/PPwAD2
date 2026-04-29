import unittest

from fib import fib, trib, tetra, fib_general


class TestFib(unittest.TestCase):
    """Testy funkcji fib()."""

    def test_fib_small_numbers(self):
        """Test fib() dla małych liczb."""
        self.assertEqual([fib(n) for n in range(6)], [0, 1, 1, 2, 3, 5])

    def test_fib_large_numbers(self):
        """Test fib(100).

        Source: https://www.wolframalpha.com/input/?i=fibonacci(100)
        """
        self.assertEqual(fib(100), 354224848179261915075)

    def test_fib_custom_start(self):
        """Test fib() z innymi wyrazami startowymi."""
        self.assertEqual([fib(n, 2, 1) for n in range(6)], [2, 1, 3, 4, 7, 11])
        self.assertEqual([fib(n, b=1, a=-1) for n in range(6)], [-1, 1, 0, 1, 1, 2])

    def test_fib_negative_n(self):
        """Test fib() dla n < 0."""
        with self.assertRaises(NotImplementedError) as context:
            fib(-1)
        self.assertEqual(
            str(context.exception), "Brak implementacji dla indeksów ujemnych"
        )


class TestTrib(unittest.TestCase):
    """Testy funkcji trib()."""

    def test_trib_small_numbers(self):
        """Test trib() dla małych liczb."""
        self.assertEqual(
            [trib(n) for n in range(10)], [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
        )

    def test_trib_large_numbers(self):
        """Test trib(37).

        Source: https://oeis.org/A000073
        """
        self.assertEqual(trib(37), 1132436852)

    def test_trib_custom_start(self):
        """Test trib() z innymi wyrazami startowymi."""
        self.assertEqual(
            [trib(n, -1, 0, 1) for n in range(10)], [-1, 0, 1, 0, 1, 2, 3, 6, 11, 20]
        )

    def test_trib_negative_n(self):
        """Test trib() dla n < 0."""
        with self.assertRaises(NotImplementedError) as context:
            trib(-1)
        self.assertEqual(
            str(context.exception), "Brak implementacji dla indeksów ujemnych"
        )


class TestFibGeneral(unittest.TestCase):
    """Testy funkcji fib_general()."""

    def test_fib_general_small_numbers(self):
        """Test fib_general() dla małych liczb."""
        self.assertEqual([fib_general(n, 1, 2) for n in range(6)], [1, 2, 3, 5, 8, 13])
        self.assertEqual(
            [fib_general(n, 1, 2, 3, -5) for n in range(10)],
            [1, 2, 3, -5, 1, 1, 0, -3, -1, -3],
        )

    def test_fib_general_large_numbers(self):
        """Test fib_general(100, *range(100))."""
        self.assertEqual(fib_general(100, *range(100)), sum(range(100)))

    def test_fib_general_too_few_arguments(self):
        """Test fib_general() z za mało argumentów startowych."""
        with self.assertRaises(TypeError):
            fib_general(5)

        with self.assertRaises(TypeError):
            fib_general(5, 1)

    def test_fib_general_negative_n(self):
        """Test fib_general() dla n < 0."""
        with self.assertRaises(NotImplementedError) as context:
            fib_general(-1, 1, 2)
        self.assertEqual(
            str(context.exception), "Brak implementacji dla indeksów ujemnych"
        )


class TestIntegrationTests(unittest.TestCase):
    """Testy integracyjne."""

    def test_fib_fibgeneral_integration(self):
        """Test fib() i fib_general() dla n = 30."""
        self.assertEqual(fib(30), fib_general(30, 0, 1))
        self.assertEqual(fib(30, 2, 1), fib_general(30, 2, 1))

    def test_trib_fibgeneral_integration(self):
        """Test trib() i fib_general() dla n = 30."""
        self.assertEqual(trib(30), fib_general(30, 0, 0, 1))
        self.assertEqual(trib(30, -1, 0, 1), fib_general(30, -1, 0, 1))

    def test_tetra_fibgeneral_integration(self):
        """Test tetra() i fib_general() dla n = 30."""
        self.assertEqual(tetra(30), fib_general(30, 0, 0, 0, 1))
        self.assertEqual(tetra(30, -1, 0, 0, 1), fib_general(30, -1, 0, 0, 1))


if __name__ == "__main__":
    unittest.main()
