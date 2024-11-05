from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WindowError(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def SetErrorWindow(self, str):
        self.setFixedSize(400, 50)
        self.setWindowTitle('BuckshotCalc: Error')
        self.Label = QLabel(str, self)
        self.Label.setFont(QFont("Arial", 12))
        self.show()