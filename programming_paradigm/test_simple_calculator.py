

import unittest

from simple_calculator import SimpleCalculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = self.calc.multiply(8, 20)
        self.assertEqual(result, 160)

    def test_divide(self):
        result = self.calc.divide(4, 2)
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

