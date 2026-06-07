"""Testy jednostkowe dla klasy Seekable z modułu seekable."""

import unittest

from seekable import Seekable


class TestSeekableIsIterator(unittest.TestCase):

    def test_has_iter_and_next(self):
        s = Seekable([1, 2, 3])
        self.assertTrue(hasattr(s, '__iter__'))
        self.assertTrue(hasattr(s, '__next__'))

    def test_iter_returns_self(self):
        s = Seekable([1, 2, 3])
        self.assertIs(iter(s), s)

    def test_usable_in_for_loop(self):
        s = Seekable([1, 2, 3])
        self.assertEqual(list(s), [1, 2, 3])


class TestSeekableLen(unittest.TestCase):

    def test_len(self):
        self.assertEqual(len(Seekable([10, 20, 30, 40, 50])), 5)

    def test_len_empty(self):
        self.assertEqual(len(Seekable([])), 0)

    def test_len_independent_of_position(self):
        s = Seekable([1, 2, 3])
        next(s)
        next(s)
        self.assertEqual(len(s), 3)


class TestSeekableNext(unittest.TestCase):

    def test_next_sequential(self):
        s = Seekable([10, 20, 30, 40, 50])
        self.assertEqual(next(s), 10)
        self.assertEqual(next(s), 20)
        self.assertEqual(next(s), 30)
        self.assertEqual(next(s), 40)
        self.assertEqual(next(s), 50)

    def test_next_raises_stop_iteration(self):
        s = Seekable([1, 2])
        next(s)
        next(s)
        with self.assertRaises(StopIteration):
            next(s)

    def test_next_empty(self):
        s = Seekable([])
        with self.assertRaises(StopIteration):
            next(s)

    def test_next_advances_position(self):
        s = Seekable([10, 20, 30])
        next(s)
        self.assertEqual(s.tell(), 1)
        next(s)
        self.assertEqual(s.tell(), 2)


class TestSeekableTell(unittest.TestCase):

    def test_initial_position(self):
        s = Seekable([1, 2, 3])
        self.assertEqual(s.tell(), 0)

    def test_after_next(self):
        s = Seekable([10, 20, 30, 40, 50])
        next(s)
        next(s)
        self.assertEqual(s.tell(), 2)

    def test_after_exhausted(self):
        s = Seekable([1, 2, 3])
        list(s)
        self.assertEqual(s.tell(), 3)


class TestSeekableSeek(unittest.TestCase):

    def test_seek_to_start(self):
        s = Seekable([10, 20, 30, 40, 50])
        list(s)
        s.seek(0)
        self.assertEqual(list(s), [10, 20, 30, 40, 50])

    def test_seek_to_middle(self):
        s = Seekable([10, 20, 30, 40, 50])
        s.seek(3)
        self.assertEqual(next(s), 40)

    def test_seek_to_end(self):
        """seek(len) jest dozwolone — kolejny next rzuca StopIteration."""
        s = Seekable([1, 2, 3])
        s.seek(3)
        self.assertEqual(s.tell(), 3)
        with self.assertRaises(StopIteration):
            next(s)

    def test_seek_updates_tell(self):
        s = Seekable([1, 2, 3, 4, 5])
        s.seek(4)
        self.assertEqual(s.tell(), 4)

    def test_seek_negative_raises_index_error(self):
        s = Seekable([1, 2, 3])
        with self.assertRaises(IndexError):
            s.seek(-1)

    def test_seek_beyond_end_raises_index_error(self):
        s = Seekable([1, 2, 3])
        with self.assertRaises(IndexError):
            s.seek(4)

    def test_seek_error_message(self):
        s = Seekable([1, 2, 3])
        with self.assertRaises(IndexError) as ctx:
            s.seek(-1)
        self.assertIn('zakres', str(ctx.exception))


class TestSeekablePeek(unittest.TestCase):

    def test_peek_does_not_advance(self):
        s = Seekable([10, 20, 30])
        self.assertEqual(s.peek(), 10)
        self.assertEqual(s.peek(), 10)
        self.assertEqual(s.tell(), 0)

    def test_peek_then_next(self):
        s = Seekable([10, 20, 30])
        self.assertEqual(s.peek(), 10)
        self.assertEqual(next(s), 10)
        self.assertEqual(s.peek(), 20)

    def test_peek_at_end_raises_stop_iteration(self):
        s = Seekable([1, 2])
        list(s)
        with self.assertRaises(StopIteration):
            s.peek()

    def test_peek_after_seek(self):
        s = Seekable([10, 20, 30, 40, 50])
        s.seek(3)
        self.assertEqual(s.peek(), 40)
        self.assertEqual(s.tell(), 3)


class TestSeekableVariousSequences(unittest.TestCase):

    def test_string(self):
        s = Seekable('abc')
        self.assertEqual(list(s), ['a', 'b', 'c'])

    def test_tuple(self):
        s = Seekable((10, 20, 30))
        self.assertEqual(next(s), 10)
        self.assertEqual(len(s), 3)

    def test_range(self):
        s = Seekable(range(5))
        self.assertEqual(list(s), [0, 1, 2, 3, 4])

    def test_does_not_modify_original(self):
        original = [1, 2, 3]
        s = Seekable(original)
        list(s)
        self.assertEqual(original, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
