import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QFontDatabase
from .window import Window


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.ui = self.window.ui
        self.setup()

    def setup(self):
        QFontDatabase.addApplicationFont('ui/fonts/Roboto/Roboto-Regular.ttf')
        font = QFont('Roboto', 1, QFont.Weight.Normal)
        self.app.setFont(font)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
