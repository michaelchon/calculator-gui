from logic.calculator import Calculator
from ui.result.result import Result


class EventHandler:
    def __init__(self, app, calculator):
        self.app = app
        self.calculator = calculator

    def on_button_click(self, event):
        try:
            event()
            self.update_result()
        except Calculator.DivisionByZero:
            self.update_result('Cannot divide by zero')
        except Calculator.InvalidOperation:
            self.update_result('Invalid operation')
        except Exception:
            self.calculator.reset()
            self.update_result('Error')

    def on_input_button_click(self, event):
        if len(self.app.ui['result'].text()) >= 17:
            return

        event()

    def update_result(self, text=None):
        if not text:
            self.app.ui['result'].setText(Result.format_number(self.calculator.current_number.value))
        else:
            self.app.ui['result'].setText(text)

        self.app.ui['result'].resize_to_fit_text()
