class CalculatorNumber:
    def __init__(self):
        self.value = '0'

    def strip_trailing_zeros(self):
        if '.' in self.value:
            self.value = self.value.rstrip('0').rstrip('.')
