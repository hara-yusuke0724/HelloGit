import unittest
import fibonacci

class Testfibobacci(unittest.TestCase):
    def test_fibobacci(self):
        self.assertEqual(fibonacci.Fibonacci(0), 0)
        self.assertEqual(fibonacci.Fibonacci(1), 0)
        self.assertEqual(fibonacci.Fibonacci(2), 1)
        self.assertEqual(fibonacci.Fibonacci(3), 1)
        self.assertEqual(fibonacci.Fibonacci(4), 2)
        self.assertEqual(fibonacci.Fibonacci(5), 3)
        self.assertEqual(fibonacci.Fibonacci(6), 5)
        self.assertEqual(fibonacci.Fibonacci(7), 8)
        self.assertEqual(fibonacci.Fibonacci(8), 13)
        self.assertEqual(fibonacci.Fibonacci(9), 21)
        self.assertEqual(fibonacci.Fibonacci(10), 34)












if __name__ == "__main__":
    unittest.main()