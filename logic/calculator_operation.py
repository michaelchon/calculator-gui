from enum import Enum, unique


@unique
class CalculatorOperation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
