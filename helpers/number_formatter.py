class NumberFormatter:
    def __init__(self, thousands_separator=' ', decimal_point=','):
        self.separator = thousands_separator
        self.decimal_point = decimal_point

        self.number = None
        self.result = []
        self.integer_digits = []
        self.i = 0
        self.formatted = None

    def format(self, number):
        self.number = number

        self.separate_thousands()
        self.format_decimal_point()

        formatted = self.formatted

        self.reset()

        return formatted

    def separate_thousands(self):
        self.result = []

        integer = self.number.split('.')[0]

        self.integer_digits = [digit for digit in integer]

        while self.integer_digits:
            self.append_digit()

        self.formatted = ''.join(reversed(self.result))

    def append_digit(self):
        self.result.append(self.integer_digits.pop())

        self.append_separator()

    def append_separator(self):
        self.i += 1

        if self.i == 3 and self.integer_digits:
            self.i = 0
            self.result.append(self.separator)

    def format_decimal_point(self):
        if len(self.number.split('.')) == 1:
            return

        fraction = self.number.split('.')[1]
        fraction = fraction.rstrip('0')
        self.formatted = self.formatted + self.decimal_point + fraction

        self.delete_redundant_decimal_point()

    def delete_redundant_decimal_point(self):
        if self.formatted.endswith(self.decimal_point):
            self.formatted = self.formatted[:-1]

    def reset(self):
        self.number = None
        self.result = []
        self.integer_digits = []
        self.i = 0
        self.formatted = None


formatter = NumberFormatter()
