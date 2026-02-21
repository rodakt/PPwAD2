import unittest


def f(seq):
    if not seq:
        raise ValueError("Empty sequence")


class Test(unittest.TestCase):

    def test_f(self):
        with self.assertRaises(ValueError) as cm:
            f([])
        print(type(cm.))
        self.assertEqual(str(cm.exception), "Empty sequence")


if __name__ == "__main__":
    unittest.main()
