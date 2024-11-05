import sys
from PyQt5.QtWidgets import *
from window import *
from windowError import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    defaultWindow = WindowDefault()
    sys.exit(app.exec())