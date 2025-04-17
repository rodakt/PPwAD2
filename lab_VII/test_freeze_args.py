"""Testy jednostkowe dla funkcji z modułu freeze_args"""

import unittest
from freeze_args import freeze_args


class TestFreezeArgs(unittest.TestCase):

    def test_freeze_args_1(self):
        def multiply(x, y):
            return x * y

        double = freeze_args(multiply, y=2)
        self.assertEqual(double(6), 12)

    def test_freeze_args_2(self):
        base16 = freeze_args(int, base=16)
        self.assertEqual(base16("A"), 10)
        self.assertEqual(base16("FF"), 15 * 16 + 15)

    def test_freeze_args_3(self):
        def f(x, y, z, *, u, v):
            return x, y, z, u, v

        g = freeze_args(f, 1, z=2, v=9)
        self.assertEqual(g(3, u=7), (1, 3, 2, 7, 9))

    def test_freeze_args_4(self):
        def f(x, y, *args, **kwargs):
            return x, y, args, kwargs

        g = freeze_args(f, 1, 2, 3, a=99, b=88)
        self.assertEqual(g(0), (1, 2, (3, 0), dict(a=99, b=88)))
        self.assertEqual(g(), (1, 2, (3,), dict(a=99, b=88)))
        self.assertEqual(g(0, c=77), (1, 2, (3, 0), dict(a=99, b=88, c=77)))


if __name__ == "__main__":
    unittest.main()
