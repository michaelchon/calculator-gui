from PyQt5.QtWidgets import QVBoxLayout
from .result.result import Result
from .buttons.buttons import Buttons


class CentralWidgetLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super(CentralWidgetLayout, self).__init__(*args, **kwargs)

        self.ui = {}
        self.setup()
        self.attach_result()
        self.attach_buttons()

    def setup(self):
        self.setContentsMargins(0, 0, 0, 0)

    def attach_result(self):
        result = Result()
        self.ui['result'] = result
        self.addWidget(result)
        self.setStretchFactor(result, 1)

    def attach_buttons(self):
        buttons = Buttons()
        self.ui.update(buttons.ui)
        self.addWidget(buttons)
        self.setStretchFactor(buttons, 4)
