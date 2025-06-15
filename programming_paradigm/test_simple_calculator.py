

import unittest

from simple_calculator import SimpleCalculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8, 20), 160)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_division_by_zero(self):
       self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()

