from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from .central_widget import CentralWidget


class Window(QMainWindow):
    min_size = (300, 465)

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setup()

        widget = CentralWidget()
        self.ui = widget.ui
        self.setCentralWidget(widget)

        self.show()

    def setup(self):
        self.setWindowTitle('Calculator')
        self.setMinimumSize(*self.min_size)
        self.resize(*self.min_size)
        self.center()

    def center(self):
        central_point = QDesktopWidget().availableGeometry().center()
        self.frameGeometry().moveCenter(central_point)
