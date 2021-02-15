""" Unit Testing for calc.py """
__author__ = 'Kanishka Wickramasinghe'


import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def test_add(self) -> None:
        """
        Tests the add method of the Calc class
        """
        self.assertEqual(Calc().add(2, 4), 6)
        self.assertEqual(Calc().add(-2, 4), 2)
        with self.assertRaises(AssertionError):
            Calc().add('d', 4)

    def test_subtract(self) -> None:
        """
        Tests the subtract method of the Calc class
        """
        self.assertEqual(Calc().subtract(2, 4), -2)
        self.assertEqual(Calc().subtract(-2, 4), -6)
        with self.assertRaises(AssertionError):
            Calc().subtract('d', 4)

    def test_multiply(self) -> None:
        """
        Tests the multiply method of the Calc class
        """
        self.assertEqual(Calc().multiply(10, 4), 40)
        self.assertEqual(Calc().multiply(-2, 0), 0)
        self.assertEqual(Calc().multiply(-2, 6), -12)
        with self.assertRaises(AssertionError):
            Calc().multiply('d', 4)

    def test_divide(self) -> None:
        """
        Tests the divide method of the Calc class
        """
        self.assertEqual(Calc().divide(2, 4), 0.5)
        self.assertEqual(Calc().divide(-2, 4), -0.5)
        self.assertEqual(Calc().divide(8, 4), 2)
        with self.assertRaises(AssertionError):
            Calc().divide('d', 4)
        with self.assertRaises(AssertionError):
            Calc().divide(2, 0)


if __name__ == '__main__':
    unittest.main()