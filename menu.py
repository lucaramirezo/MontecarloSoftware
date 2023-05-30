# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets
# Important:
# You need to run the following command to generate the ui_menu.py file
#     pyside6-uic menu.ui -o ui_menu.py, or
#     pyside2-uic menu.ui -o ui_menu.py
from ui_menu import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
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
        self.ui.frame_superior.mouseMoveEvent = mouseMoveEvent
        # Acceder a las páginas
        self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageTask))
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageBudget))
        self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageUsers))
        self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageSettings))
        self.ui.bt_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageHelp))
        self.ui.bt_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))
        # Control de la barra de título
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(self.close)
        self.ui.bt_restaurar.hide()

        # Menú lateral

        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        width = self.ui.frame_lateral.width()
        normal = 0
        if width == 0:
            extender = 200
        else:
            extender = normal
        self.animacion = QtCore.QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(350)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

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
    def editar_tabla(self):
        self.qtablewidgetitem.setitem(0,0,TableWidgetItem())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
