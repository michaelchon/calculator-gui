from functools import partial
from event_handler import EventHandler


class EventConnector:
    def __init__(self, app, calculator):
        self.app = app
        self.calculator = calculator
        self.event_handler = EventHandler(app, calculator)

    def connect_events(self):
        self.connect_input_buttons()
        self.connect_delete_buttons()
        self.connect_basic_operation_buttons()
        self.connect_special_operation_buttons()
        self.connect_calculate_button()

    def connect_input_buttons(self):
        for i in range(10):
            self.connect_input_button(f'digit{i}_button', partial(self.calculator.add_digit, i))

        self.connect_input_button('period_button', self.calculator.add_period)

    def connect_input_button(self, button, event):
        self.connect_button(button, partial(self.event_handler.on_input_button_click, event))

    def connect_delete_buttons(self):
        self.connect_button('reset_current_number_button', self.calculator.reset_current_number)
        self.connect_button('reset_button', self.calculator.reset)
        self.connect_button('delete_last_entity_button', self.calculator.delete_last_entity)

    def connect_basic_operation_buttons(self):
        self.connect_button('divide_button', self.calculator.prepare_divide_operation)
        self.connect_button('multiply_button', self.calculator.prepare_multiply_operation)
        self.connect_button('subtract_button', self.calculator.prepare_subtract_operation)
        self.connect_button('add_button', self.calculator.prepare_add_operation)

    def connect_special_operation_buttons(self):
        self.connect_button('percent_button', self.calculator.percent)
        self.connect_button('invert_button', self.calculator.invert)
        self.connect_button('square_button', self.calculator.square)
        self.connect_button('square_root_button', self.calculator.square_root)
        self.connect_button('negate_button', self.calculator.negate)

    def connect_calculate_button(self):
        self.connect_button('calculate_button', self.calculator.calculate)

    def connect_button(self, button, event):
        self.app.ui[button].clicked.connect(partial(self.event_handler.on_button_click, event))
