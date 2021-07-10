import unittest
from logic.calculator_number import CalculatorNumber


class TestCalculatorNumber(unittest.TestCase):
    def setUp(self):
        self.number = CalculatorNumber()

    def test_strip_trailing_zeros_in_decimal(self):
        self.number.value = '95.600'
        self.number.strip_trailing_zeros()

        self.assertEqual(self.number.value, '95.6')

    def test_strip_trailing_zeros_in_integer(self):
        self.number.value = '95'
        self.number.strip_trailing_zeros()

        self.assertEqual(self.number.value, '95')


if __name__ == '__main__':
    unittest.main()
