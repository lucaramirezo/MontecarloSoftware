# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuUser.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.441, y1:0, x2:0.514851, y2:1, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.frame_superior.setLineWidth(1)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(1, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        self.bt_menu.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.bt_menu.setFont(font)
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.441, y1:0, x2:0.514851, y2:1, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 87 12pt \"Arial Narrow\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Narrow\";\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../MontecarloSoftware/Media/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(35, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:4px solid rgb(85, 85, 255);\n"
"background-color:#ffff00;\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../MontecarloSoftware/Media/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))
        self.bt_minimizar.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_minimizar, 0, Qt.AlignRight)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(35, 35))
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:4px solid rgb(85, 85, 255);\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../MontecarloSoftware/Media/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.bt_restaurar, 0, Qt.AlignRight)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(35, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:4px solid rgb(85, 85, 255);\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../MontecarloSoftware/Media/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_maximizar, 0, Qt.AlignRight)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:4px solid rgb(85, 85, 255);\n"
"background-color:red;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../MontecarloSoftware/Media/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_cerrar, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(200, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:1, y2:0.545, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:1, y2:0.545, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"../MontecarloSoftware/Media/taskC.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_uno = QPushButton(self.frame_lateral)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setMinimumSize(QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../MontecarloSoftware/Media/budget.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon6)
        self.bt_uno.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_uno)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_tres = QPushButton(self.frame_lateral)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setMinimumSize(QSize(0, 40))
        self.bt_tres.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"../MontecarloSoftware/Media/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_tres.setIcon(icon7)
        self.bt_tres.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_tres)

        self.bt_cuatro = QPushButton(self.frame_lateral)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setMinimumSize(QSize(0, 40))
        self.bt_cuatro.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"../MontecarloSoftware/Media/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cuatro.setIcon(icon8)
        self.bt_cuatro.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cuatro)

        self.bt_cinco = QPushButton(self.frame_lateral)
        self.bt_cinco.setObjectName(u"bt_cinco")
        self.bt_cinco.setMinimumSize(QSize(0, 40))
        self.bt_cinco.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"../MontecarloSoftware/Media/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cinco.setIcon(icon9)
        self.bt_cinco.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cinco)


        self.horizontalLayout.addWidget(self.frame_lateral, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.frame_inferior)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.pageTask = QWidget()
        self.pageTask.setObjectName(u"pageTask")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageTask.sizePolicy().hasHeightForWidth())
        self.pageTask.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.pageTask)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.pageTask)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_22 = QVBoxLayout(self.widget_7)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.widget_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 87 15pt \"Arial Black\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_6)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(20)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-color:rgb(0, 0, 0);\n"
"background-color: rgb(85, 85, 255);\n"
"border-radius: 5px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 2px;\n"
"border-bottom-left-radius: 2px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_20.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_6 = QPushButton(self.widget_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.EditList_2 = QPushButton(self.widget_8)
        self.EditList_2.setObjectName(u"EditList_2")

        self.horizontalLayout_6.addWidget(self.EditList_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addWidget(self.widget_8)

        self.horizontalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_19.addItem(self.horizontalSpacer_3)

        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(150)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.widget_9)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_3.rowCount() < 3):
            self.tableWidget_3.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_21.addWidget(self.tableWidget_3)


        self.verticalLayout_19.addWidget(self.widget_9)


        self.verticalLayout_22.addWidget(self.frame_2)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.pageTask)
        self.pageBudget = QWidget()
        self.pageBudget.setObjectName(u"pageBudget")
        sizePolicy.setHeightForWidth(self.pageBudget.sizePolicy().hasHeightForWidth())
        self.pageBudget.setSizePolicy(sizePolicy)
        self.pageBudget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.pageBudget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.pageBudget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_17 = QVBoxLayout(self.widget_4)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"font: 87 15pt \"Arial Black\";\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_5)

        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.widget_5.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-color:rgb(0, 0, 0);\n"
"background-color: rgb(85, 85, 255);\n"
"border-radius: 5px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 2px;\n"
"border-bottom-left-radius: 2px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_5 = QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.EditList = QPushButton(self.widget_5)
        self.EditList.setObjectName(u"EditList")

        self.horizontalLayout_2.addWidget(self.EditList)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_16.addWidget(self.widget_5)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_2)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.tableWidget = QTableWidget(self.widget_6)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_16.addWidget(self.widget_6)


        self.verticalLayout_17.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.pageBudget)
        self.pageUsers = QWidget()
        self.pageUsers.setObjectName(u"pageUsers")
        sizePolicy.setHeightForWidth(self.pageUsers.sizePolicy().hasHeightForWidth())
        self.pageUsers.setSizePolicy(sizePolicy)
        self.pageUsers.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.pageUsers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 1, 1, 1)
        self.stackedWidget.addWidget(self.pageUsers)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        sizePolicy.setHeightForWidth(self.pageSettings.sizePolicy().hasHeightForWidth())
        self.pageSettings.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.widget = QWidget(self.pageSettings)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_13 = QVBoxLayout(self.widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 87 27pt \"Arial Black\";")

        self.verticalLayout_13.addWidget(self.label_2)

        self.widgetEmail = QWidget(self.widget)
        self.widgetEmail.setObjectName(u"widgetEmail")
        self.verticalLayout_10 = QVBoxLayout(self.widgetEmail)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelEmain = QLabel(self.widgetEmail)
        self.labelEmain.setObjectName(u"labelEmain")
        self.labelEmain.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_10.addWidget(self.labelEmain)

        self.lineEditEmail = QLineEdit(self.widgetEmail)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.lineEditEmail)


        self.verticalLayout_13.addWidget(self.widgetEmail)

        self.widgetPhone = QWidget(self.widget)
        self.widgetPhone.setObjectName(u"widgetPhone")
        self.verticalLayout_11 = QVBoxLayout(self.widgetPhone)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelPhone = QLabel(self.widgetPhone)
        self.labelPhone.setObjectName(u"labelPhone")
        self.labelPhone.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_11.addWidget(self.labelPhone)

        self.lineEditPhone = QLineEdit(self.widgetPhone)
        self.lineEditPhone.setObjectName(u"lineEditPhone")
        self.lineEditPhone.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.lineEditPhone)


        self.verticalLayout_13.addWidget(self.widgetPhone)

        self.widgetAddress = QWidget(self.widget)
        self.widgetAddress.setObjectName(u"widgetAddress")
        self.verticalLayout_12 = QVBoxLayout(self.widgetAddress)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelAddress = QLabel(self.widgetAddress)
        self.labelAddress.setObjectName(u"labelAddress")
        self.labelAddress.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_12.addWidget(self.labelAddress)

        self.lineEditAddress = QLineEdit(self.widgetAddress)
        self.lineEditAddress.setObjectName(u"lineEditAddress")
        self.lineEditAddress.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.lineEditAddress)


        self.verticalLayout_13.addWidget(self.widgetAddress)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.pageSettings)
        self.pageHelp = QWidget()
        self.pageHelp.setObjectName(u"pageHelp")
        sizePolicy.setHeightForWidth(self.pageHelp.sizePolicy().hasHeightForWidth())
        self.pageHelp.setSizePolicy(sizePolicy)
        self.pageHelp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QVBoxLayout(self.pageHelp)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.widget_2 = QWidget(self.pageHelp)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 87 25pt \"Arial Black\";")

        self.verticalLayout_15.addWidget(self.label_3)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_14 = QVBoxLayout(self.widget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 87 14pt \"Arial Black\";")

        self.verticalLayout_14.addWidget(self.label_4)

        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_14.addWidget(self.textEdit)


        self.verticalLayout_15.addWidget(self.widget_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.pageHelp)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        sizePolicy.setHeightForWidth(self.page_cinco.sizePolicy().hasHeightForWidth())
        self.page_cinco.setSizePolicy(sizePolicy)
        self.page_cinco.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cinco)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.page_cinco)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"font: 87 36pt \"Arial Black\";")

        self.verticalLayout_8.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page_cinco)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.frame_contenedor.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bt_menu.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"Task Management", None))
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"Budget Management", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.bt_cuatro.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.bt_cinco.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Task Management", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Search List", None))
        self.EditList_2.setText(QCoreApplication.translate("MainWindow", u"EditList", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Estimated minimun", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Estimated maximun", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Estimated time", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem4 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nouvelle ligne", None));
        ___qtablewidgetitem5 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Task1", None));
        ___qtablewidgetitem6 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Task3", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Budget Management", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Search List", None))
        self.EditList.setText(QCoreApplication.translate("MainWindow", u"EditList", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Estimated minimun", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Estimated maximun", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Estimated time", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Bugdet1", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Budget2", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Bugdet3", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Budget4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Account Settings", None))
        self.labelEmain.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.lineEditEmail.setText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.labelPhone.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEditPhone.setText(QCoreApplication.translate("MainWindow", u"672154987", None))
        self.labelAddress.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEditAddress.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to help page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ask us something, we\u00b4ll respond via Email", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

