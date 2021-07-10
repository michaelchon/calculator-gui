from PyQt5.QtWidgets import QWidget
from .central_widget_layout import CentralWidgetLayout


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(CentralWidget, self).__init__(*args, **kwargs)

        layout = CentralWidgetLayout()
        self.ui = layout.ui
        self.setLayout(layout)
