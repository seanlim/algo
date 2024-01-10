import unittest

from Solution import Solution

solution = Solution()


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual("III", solution.intToRoman(3))

    def test_2(self):
        self.assertEqual("LVIII", solution.intToRoman(58))

    def test_3(self):
        self.assertEqual("MCMXCIV", solution.intToRoman(1994))

    def test_4(self):
        self.assertEqual("MMI", solution.intToRoman(2001))

    def test_5(self):
        self.assertEqual("MCMXCIX", solution.intToRoman(1999))

    def test_6(self):
        self.assertEqual("MMMCMXCIX", solution.intToRoman(3999))


if __name__ == '__main__':
    unittest.main()
