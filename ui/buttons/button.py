from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self.setup()

    def setup(self):
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        font = self.font()
        font.setPixelSize(20)
        self.setFont(font)
