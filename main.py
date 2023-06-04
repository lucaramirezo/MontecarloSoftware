# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets
# Important:
# You need to run the following command to generate the ui_menu.py file
#     pyside6-uic menu.ui -o ui_menu.py, or
#     pyside2-uic menu.ui -o ui_menu.py
from ui_AdminMainView import Ui_AdminMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdminMainWindow()
        self.ui.setupUi(self)
# Eliminar barra de título y establecer opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # Mover ventana
        def mouseMoveEvent(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.admin_main_panel.mouseMoveEvent = mouseMoveEvent
        # Acceder a las páginas
        self.ui.bt_task.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.task_card))
        self.ui.bt_budget.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.budget_card))
        self.ui.bt_users.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.users_card))
        self.ui.bt_settings.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.settings_card))
        self.ui.bt_help.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.help_card))
        self.ui.bt_log_out.clicked.connect(lambda: self.ui.central_card_container.setCurrentWidget(self.ui.lo_out_card))
        # Control de la barra de título
        self.ui.bt_min.clicked.connect(self.control_bt_minimizar)
        self.ui.bt_restore.clicked.connect(self.control_bt_normal)
        self.ui.bt_max.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_close.clicked.connect(self.close)
        self.ui.bt_restore.hide()

        # Menú lateral

        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.bt_restore.hide()
        self.ui.bt_max.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.bt_max.hide()
        self.ui.bt_restore.show()

    def mover_menu(self):
        width = self.ui.menu_bar.width()
        normal = 0
        if width == 0:
            extender = 200
        else:
            extender = normal

        self.animacion = QtCore.QPropertyAnimation(self.ui.menu_bar, b'minimumWidth')
        self.animacion.setDuration(350)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

        # Desplazar el contenido hacia la izquierda
        content_position = self.ui.menu_bar.pos()
        content_width = self.ui.menu_bar.width()
        if extender == 0:
            # Ocultar el menú lateral, desplazar el contenido hacia la izquierda
            self.animacion_content = QtCore.QPropertyAnimation(self.ui.menu_bar, b'pos')
            self.animacion_content.setDuration(350)
            self.animacion_content.setStartValue(content_position)
            self.animacion_content.setEndValue(QtCore.QPoint(-extender, content_position.y()))
            self.animacion_content.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion_content.start()
        else:
            # Mostrar el menú lateral, desplazar el contenido hacia la derecha
            self.animacion_content = QtCore.QPropertyAnimation(self.ui.menu_bar, b'pos')
            self.animacion_content.setDuration(350)
            self.animacion_content.setStartValue(content_position)
            self.animacion_content.setEndValue(QtCore.QPoint(normal, content_position.y()))
            self.animacion_content.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion_content.start()

    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition() - self.clickPosition)
                self.clickPosition = event.globalPosition()
                event.accept()

        if event.globalPosition().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
