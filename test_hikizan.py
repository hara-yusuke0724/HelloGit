import unittest
from hikizan import hikizan


class TestTashizan(unittest.TestCase):
    """test class of hikizan.py
    """

    def test_hikizan(self):
        """test method for hikizan
        """
        value1 = 7
        value2 = 3
        expected = 4
        actual = hikizan(value1,value2)
        self.assertEqual(expected, actual)


if __name__== "__main__":
    unittest.main()