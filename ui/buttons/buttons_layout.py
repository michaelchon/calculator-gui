from PyQt5.QtWidgets import QGridLayout


class ButtonsLayout(QGridLayout):
    def __init__(self, *args, **kwargs):
        super(ButtonsLayout, self).__init__(*args, **kwargs)

        self.setup()

    def setup(self):
        self.setHorizontalSpacing(2)
        self.setVerticalSpacing(2)
        self.setContentsMargins(0, 0, 0, 0)
