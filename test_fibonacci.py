import unittest
import fibonacci
class Testfibobacci(unittest.TestCase):
    def test_fibobacci(self):
            v1 = Fibonacci(n-1)
            v2 = Fibonacci(n-2)
            expected = Fibonacci(n-1)+Fibonacci(n-2)
            actual = fibonacci(v1,v2)
            self.asserEqual(expected,actual)


    if __name__ == "__main__":
            unittest.main()