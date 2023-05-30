# This Python file uses the following encoding: utf-8
import sys

import mariadb
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore, QtWidgets

from Modelo.DAO import DAO
from Modelo.User import User
# Important:
# You need to run the following command to generate the ui_menu.py file
#     pyside6-uic menu.ui -o ui_menu.py, or
#     pyside2-uic menu.ui -o ui_menu.py
from ui_loginWindow import Ui_MainWindow





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def create_user(self):
        username = self.ui.Username_LineEdit.text()
        password = self.ui.Password_LineEdit.text()

        try:
            if username and password:
                self.__create_user_in_ddbb(username, password)
        except mariadb.Error as e:
            error_message = str(e)
            QMessageBox.warning(self, "Error", f"Login already exists: {error_message}")
            return
        self.ui.Username_LineEdit.clear()
        self.ui.Password_LineEdit.clear()

    @staticmethod
    def __create_user_in_ddbb(username, password):
        dao = DAO.get_instance(host='195.235.211.195', user='psi_grupo6', password='50K2f#k!wg^M')
        if dao.check_user_exists(username):
            raise mariadb.Error("User already exists")

        user = User(login=username, password=password)
        user.cipher_password()

        dao.create_user(user)

        dao.close_connection()

    def login_user(self):
        username = self.ui.Username_LineEdit.text()
        password = self.ui.Password_LineEdit.text()

        dao = DAO.get_instance()
        user = dao.login_user(username, password)
        if user is None:
            QMessageBox.warning(self, "Error", f"Incorrect password or username")
            return
        # todo hacer algo con el objeto user que se ha devuelto


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
