import unittest
from unittest.mock import patch
from logic.calculator import Calculator
from logic.calculator_operation import CalculatorOperation
from logic.calculator_history_item import CalculatorHistoryItem


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_digit(self):
        self.calculator.add_digit(8)
        self.calculator.add_digit(9)

        self.assertEqual(self.calculator.current_number.value, '89')

    def test_add_digit_passing_not_digit(self):
        self.assertRaises(Calculator.NotDigit, self.calculator.add_digit, 18)

    def test_add_digit_passing_not_number(self):
        self.assertRaises(Calculator.WrongArgumentType, self.calculator.add_digit, None)

    def test_add_period(self):
        self.calculator.add_period()

        self.assertEqual(self.calculator.current_number.value, '0.')

    def test_add_period_two_times(self):
        self.calculator.add_period()
        self.calculator.add_period()

        self.assertEqual(self.calculator.current_number.value, '0.')

    def test_reset(self):
        self.calculator.add_digit(8)
        self.calculator.prepare_add_operation()
        self.calculator.add_digit(5)
        self.calculator.reset()

        self.assertEqual(self.calculator.number1.value, '0')
        self.assertEqual(self.calculator.number2.value, '0')
        self.assertIs(self.calculator.current_number, self.calculator.number1)
        self.assertEqual(self.calculator.operation, None)

    def test_reset_current_number(self):
        self.calculator.add_digit(8)
        self.calculator.prepare_add_operation()
        self.calculator.add_digit(5)
        self.calculator.reset_current_number()

        self.assertEqual(self.calculator.number1.value, '8')
        self.assertEqual(self.calculator.number2.value, '0')
        self.assertIs(self.calculator.current_number, self.calculator.number2)
        self.assertEqual(self.calculator.operation, CalculatorOperation.ADD)

    def test_delete_last_entity(self):
        self.calculator.add_digit(8)
        self.calculator.add_digit(5)
        self.calculator.add_period()
        self.calculator.add_digit(2)
        self.calculator.delete_last_entity()
        self.calculator.delete_last_entity()
        self.calculator.delete_last_entity()

        self.assertEqual(self.calculator.current_number.value, '8')

    def test_delete_only_digit(self):
        self.calculator.delete_last_entity()

        self.assertEqual(self.calculator.current_number.value, '0')

    def test_prepare_operation_passing_not_operation(self):
        self.assertRaises(Calculator.WrongArgumentType, self.calculator.prepare_operation, None)

    def test_prepare_operation_as_first_operation(self):
        with patch.object(Calculator, 'calculate') as mock_calculate:
            self.calculator.prepare_operation(CalculatorOperation.SUBTRACT)

            mock_calculate.assert_not_called()

    def test_prepare_operation_after_another_operation(self):
        with patch.object(Calculator, 'calculate') as mock_calculate:
            self.calculator.operation = CalculatorOperation.ADD
            self.calculator.prepare_operation(CalculatorOperation.SUBTRACT)

            mock_calculate.assert_called_once()

    def test_prepare_add_operation(self):
        self.calculator.prepare_add_operation()

        self.assertEqual(self.calculator.operation, CalculatorOperation.ADD)
        self.assertEqual(self.calculator.current_number, self.calculator.number2)

    def test_prepare_subtract_operation(self):
        self.calculator.prepare_subtract_operation()

        self.assertEqual(self.calculator.operation, CalculatorOperation.SUBTRACT)
        self.assertEqual(self.calculator.current_number, self.calculator.number2)

    def test_prepare_multiply_operation(self):
        self.calculator.prepare_multiply_operation()

        self.assertEqual(self.calculator.operation, CalculatorOperation.MULTIPLY)
        self.assertEqual(self.calculator.current_number, self.calculator.number2)

    def test_prepare_divide_operation(self):
        self.calculator.prepare_divide_operation()

        self.assertEqual(self.calculator.operation, CalculatorOperation.DIVIDE)
        self.assertEqual(self.calculator.current_number, self.calculator.number2)

    def test_calculate(self):
        self.calculator.add_digit(4)
        self.calculator.add_period()
        self.calculator.add_digit(2)
        self.calculator.prepare_add_operation()
        self.calculator.add_digit(5)
        self.calculator.prepare_subtract_operation()
        self.calculator.add_digit(3)
        self.calculator.add_period()
        self.calculator.add_digit(2)
        self.calculator.calculate()

        self.assertEqual(self.calculator.number1.value, '6')
        self.assertEqual(self.calculator.number2.value, '0')
        self.assertIs(self.calculator.current_number, self.calculator.number1)
        self.assertEqual(self.calculator.operation, None)
        self.assertListEqual(list(map(vars, self.calculator.history.items)),
                             list(map(vars, [CalculatorHistoryItem('4.2', CalculatorOperation.ADD, '5', '9.2'),
                                             CalculatorHistoryItem('9.2', CalculatorOperation.SUBTRACT, '3.2', '6')])))

    def test_calculate_immediately(self):
        self.calculator.calculate()

        self.assertEqual(self.calculator.number1.value, '0')
        self.assertEqual(self.calculator.number2.value, '0')
        self.assertIs(self.calculator.current_number, self.calculator.number1)
        self.assertEqual(self.calculator.operation, None)

    def test_calculate_zero_division(self):
        self.calculator.add_digit(8)
        self.calculator.prepare_divide_operation()
        self.calculator.add_digit(0)

        self.assertRaises(Calculator.DivisionByZero, self.calculator.calculate)

    def test_percent_number1(self):
        self.calculator.add_digit(9)
        self.calculator.add_digit(5)
        self.calculator.percent()

        self.assertIs(self.calculator.current_number, self.calculator.number1)
        self.assertEqual(self.calculator.current_number.value, '0.95')

    def test_percent_number2(self):
        self.calculator.add_digit(2)
        self.calculator.add_digit(0)
        self.calculator.add_digit(0)
        self.calculator.prepare_add_operation()
        self.calculator.add_digit(5)
        self.calculator.percent()

        self.assertIs(self.calculator.current_number, self.calculator.number2)
        self.assertEqual(self.calculator.current_number.value, '10')

    def test_invert(self):
        self.calculator.add_digit(1)
        self.calculator.add_digit(0)
        self.calculator.invert()

        self.assertEqual(self.calculator.current_number.value, '0.1')

    def test_invert_zero(self):
        self.calculator.add_digit(0)

        self.assertRaises(Calculator.DivisionByZero, self.calculator.invert)

    def test_square(self):
        self.calculator.add_digit(8)
        self.calculator.square()

        self.assertEqual(self.calculator.current_number.value, '64')

    def test_square_root(self):
        self.calculator.add_digit(9)
        self.calculator.square_root()

        self.assertEqual(self.calculator.current_number.value, '3')

    def test_square_root_of_negative_number(self):
        self.calculator.prepare_subtract_operation()
        self.calculator.add_digit(8)
        self.calculator.calculate()

        self.assertRaises(Calculator.InvalidOperation, self.calculator.square_root)

    def test_negate_positive(self):
        self.calculator.add_digit(8)
        self.calculator.negate()

        self.assertEqual(self.calculator.current_number.value, '-8')

    def test_negate_negative(self):
        self.calculator.prepare_subtract_operation()
        self.calculator.add_digit(8)
        self.calculator.calculate()
        self.calculator.negate()

        self.assertEqual(self.calculator.current_number.value, '8')


if __name__ == '__main__':
    unittest.main()
