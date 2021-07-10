import decimal
from decimal import Decimal
from logic.calculator_number import CalculatorNumber
from logic.calculator_operation import CalculatorOperation
from logic.calculator_history import CalculatorHistory
from logic.calculator_history_item import CalculatorHistoryItem


class Calculator:
    def __init__(self):
        decimal.getcontext().prec = 14
        self.number1 = CalculatorNumber()
        self.number2 = CalculatorNumber()
        self.current_number = self.number1
        self.operation = None
        self.history = CalculatorHistory()

    def add_digit(self, digit):
        self.validate_digit(digit)

        if self.current_number.value == '0':
            self.current_number.value = str(digit)
        elif self.current_number.value == '-0':
            self.current_number.value = '-' + str(digit)
        else:
            self.current_number.value += str(digit)

    def validate_digit(self, digit):
        if type(digit) != int and type(digit) != float:
            raise self.WrongArgumentType('An integer or float must be passed.')

        if digit < 0 or digit > 9:
            raise self.NotDigit('A number from 1 to 9 must be passed.')

    def add_period(self):
        if '.' not in self.current_number.value:
            self.current_number.value += '.'

    def reset(self):
        self.number1.value = '0'
        self.number2.value = '0'
        self.current_number = self.number1
        self.operation = None

    def reset_current_number(self):
        self.current_number.value = '0'

    def delete_last_entity(self):
        if len(self.current_number.value) > 1:
            self.current_number.value = self.current_number.value[:-1]
        else:
            self.current_number.value = '0'

    def prepare_operation(self, operation):
        if not isinstance(operation, CalculatorOperation):
            raise self.WrongArgumentType('Instance of CalculatorOperation must be passed.')

        if self.operation is not None:
            self.calculate()

        self.operation = operation
        self.current_number = self.number2

    def prepare_add_operation(self):
        self.prepare_operation(CalculatorOperation.ADD)

    def prepare_subtract_operation(self):
        self.prepare_operation(CalculatorOperation.SUBTRACT)

    def prepare_multiply_operation(self):
        self.prepare_operation(CalculatorOperation.MULTIPLY)

    def prepare_divide_operation(self):
        self.prepare_operation(CalculatorOperation.DIVIDE)

    def calculate(self):
        history_number1 = self.number1.value

        if self.operation == CalculatorOperation.ADD:
            self.number1.value = str(Decimal(self.number1.value) + Decimal(self.number2.value))
        elif self.operation == CalculatorOperation.SUBTRACT:
            self.number1.value = str(Decimal(self.number1.value) - Decimal(self.number2.value))
        elif self.operation == CalculatorOperation.MULTIPLY:
            self.number1.value = str(Decimal(self.number1.value) * Decimal(self.number2.value))
        elif self.operation == CalculatorOperation.DIVIDE:
            self.divide()
        else:
            return

        self.number1.strip_trailing_zeros()

        self.history.items.append(
            CalculatorHistoryItem(history_number1, self.operation, self.number2.value, self.number1.value))

        self.number2.value = '0'
        self.current_number = self.number1
        self.operation = None

    def divide(self):
        try:
            self.number1.value = str(Decimal(self.number1.value) / Decimal(self.number2.value))
        except decimal.DivisionByZero:
            raise self.DivisionByZero('Cannot divide by zero.')

    def percent(self):
        if self.current_number is self.number1:
            self.current_number.value = str(Decimal(self.current_number.value) / 100)
        else:
            self.current_number.value = str(Decimal(self.number1.value) / 100 * Decimal(self.number2.value))

    def invert(self):
        try:
            self.current_number.value = str(1 / Decimal(self.current_number.value))
        except decimal.DivisionByZero:
            raise self.DivisionByZero('Cannot invert zero.')

    def square(self):
        self.current_number.value = str(Decimal(self.current_number.value) ** 2)

    def square_root(self):
        try:
            self.current_number.value = str(Decimal(self.current_number.value).sqrt())
        except decimal.InvalidOperation:
            raise self.InvalidOperation('Cannot get square root of negative number.')

    def negate(self):
        self.current_number.value = str(Decimal(self.current_number.value).copy_negate())

    class WrongArgumentType(TypeError):
        pass

    class NotDigit(ValueError):
        pass

    class DivisionByZero(ZeroDivisionError):
        pass

    class InvalidOperation(ValueError):
        pass
