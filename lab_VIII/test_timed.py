"""Testy dla dekoratora timed z pliku timed.py"""

import unittest
from unittest.mock import patch, MagicMock
import io
import sys
from timed import timed

class TestTimed(unittest.TestCase):
    """Testy dla dekoratora mierzącego czas."""

    def test_metadata_preservation(self):
        """Sprawdza, czy dekorator zachowuje metadane funkcji."""
        @timed(repeat=2)
        def example_func():
            """Dokumentacja testowa."""
            return True
        
        self.assertEqual(example_func.__name__, "example_func")
        self.assertEqual(example_func.__doc__, "Dokumentacja testowa.")

    def test_return_value(self):
        """Sprawdza, czy dekorator zwraca wynik ostatniego wywołania."""
        call_count = 0
        @timed(repeat=3)
        def incremental_func():
            nonlocal call_count
            call_count += 1
            return call_count
        
        # Przechwytujemy stdout, żeby nie śmiecić w konsoli podczas testu
        with patch('sys.stdout', new=io.StringIO()):
            result = incremental_func()
        
        self.assertEqual(result, 3)

    def test_repeat_count(self):
        """Sprawdza, czy funkcja jest wywoływana dokładnie tyle razy, ile zadano."""
        mock_func = MagicMock(return_value=None)
        mock_func.__name__ = "mock_func"
        decorated = timed(repeat=10)(mock_func)
        
        with patch('sys.stdout', new=io.StringIO()):
            decorated()
            
        self.assertEqual(mock_func.call_count, 10)

    @patch('time.perf_counter')
    def test_output_format_and_stats(self, mock_perf):
        """Sprawdza format wypisywanego komunikatu i poprawność obliczeń statystycznych."""
        # Symulujemy czasy trwania kolejnych wywołań: 1.0s, 2.0s, 3.0s
        # perf_counter musi zwracać wartości narastające dla start i end każdego wywołania
        # Wywołanie 1: start=0, end=1.0 (czas 1.0)
        # Wywołanie 2: start=2, end=4.0 (czas 2.0)
        # Wywołanie 3: start=5, end=8.0 (czas 3.0)
        mock_perf.side_effect = [0.0, 1.0, 2.0, 4.0, 5.0, 8.0]
        
        @timed(repeat=3)
        def slow_func():
            pass
            
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            slow_func()
            
        output = captured_output.getvalue().strip()
        
        # Oczekiwane statystyki dla [1.0, 2.0, 3.0]:
        # mean = (1+2+3)/3 = 2.0
        # stdev = sqrt(((1-2)^2 + (2-2)^2 + (3-2)^2) / (3-1)) = sqrt(2/2) = 1.0
        
        self.assertIn("slow_func (repeat=3):", output)
        self.assertIn("mean=2.0000 s", output)
        self.assertIn("stdev=1.0000 s", output)

if __name__ == "__main__":
    unittest.main()
