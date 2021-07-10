import json
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
from .buttons_layout import ButtonsLayout
from .button import Button


class Buttons(QWidget):
    def __init__(self, *args, **kwargs):
        super(Buttons, self).__init__(*args, **kwargs)

        with open('ui/buttons/buttons.json', encoding='utf-8') as f:
            self.names = json.load(f)['buttons']
        self.ui = {}
        self.layout = ButtonsLayout()
        self.setup()
        self.populate()

    def setup(self):
        self.setLayout(self.layout)
        with open('ui/buttons/button.css') as f:
            self.setStyleSheet(f.read())

    def populate(self):
        for x, row in enumerate(self.names):
            for y, column in enumerate(row):
                self.create_button(column, x, y)

    def create_button(self, column, x, y):
        button = Button(column['text'])
        key = column['key']
        if key == 'calculate_button':
            with open('ui/buttons/calculate_button.css') as f:
                button.setStyleSheet(f.read())
        elif key == 'delete_last_entity_button':
            button.setIcon(QIcon('ui/buttons/delete.png'))

        font = button.font()
        if not key.startswith('digit'):
            font.setWeight(QFont.Weight.Light)
        else:
            font.setWeight(QFont.Weight.Medium)
        button.setFont(font)

        self.ui[key] = button
        self.layout.addWidget(button, x, y)
