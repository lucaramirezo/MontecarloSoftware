import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets
# Important:
# You need to run the following command to generate the ui_menu.py file
#     pyside6-uic menu.ui -o ui_menu.py, or
#     pyside2-uic menu.ui -o ui_menu.py
from ui_Login import Ui_LoginWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())