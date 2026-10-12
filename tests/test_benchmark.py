"""Unit tests for utility functions."""
import unittest
from utils.benchmark import timing_decorator

class TestBenchmark(unittest.TestCase):
    def test_timing_decorator(self):
        @timing_decorator
        def add(a, b):
            return a + b
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    unittest.main()
