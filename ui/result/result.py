from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFontMetrics, QFont
from helpers.number_formatter import formatter


class Result(QLabel):
    default_font_size_px = 50

    def __init__(self, *args, **kwargs):
        super(Result, self).__init__(*args, **kwargs)

        self.setup()

    def setup(self):
        self.setText('0')
        with open('ui/result/result.css') as f:
            self.setStyleSheet(f.read())
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        font = self.font()
        font.setPixelSize(self.default_font_size_px)
        self.setFont(font)

    def resize_to_fit_text(self):
        content_width = self.contentsRect().width() - 30

        font = self.font()
        font.setWeight(QFont.Weight.Medium)

        if self.font_width(font) > content_width:
            while self.font_width(font) > content_width and font.pixelSize() > 1:
                font.setPixelSize(font.pixelSize() - 1)
        elif self.font_width(font) < content_width:
            while self.font_width(font) < content_width and font.pixelSize() < self.default_font_size_px:
                font.setPixelSize(font.pixelSize() + 1)
            if self.font_width(font) > content_width:
                font.setPixelSize(font.pixelSize() - 1)

        self.setFont(font)

    def resizeEvent(self, a0):
        self.resize_to_fit_text()

    def font_width(self, font):
        return QFontMetrics(font).boundingRect(self.contentsRect(), self.alignment(), self.text()).width()

    @staticmethod
    def format_number(number):
        return formatter.format(number)
