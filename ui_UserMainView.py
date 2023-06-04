# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserMainView.ui'
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

class Ui_UserMainWindow(object):
    def setupUi(self, UserMainWindow):
        if not UserMainWindow.objectName():
            UserMainWindow.setObjectName(u"UserMainWindow")
        UserMainWindow.resize(800, 600)
        self.user_main_panel = QWidget(UserMainWindow)
        self.user_main_panel.setObjectName(u"user_main_panel")
        self.verticalLayout = QVBoxLayout(self.user_main_panel)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.user_main_panel)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(0, 35))
        self.menu_bar.setMaximumSize(QSize(16777215, 50))
        self.menu_bar.setStyleSheet(u"QFrame{\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.441, y1:0, x2:0.514851, y2:1, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.menu_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.menu_bar.setLineWidth(1)
        self.horizontalLayout_8 = QHBoxLayout(self.menu_bar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(1, 0, 0, 0)
        self.bt_menu = QPushButton(self.menu_bar)
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
        icon.addFile(u"Media/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_menu)

        self.menu_bar_spacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.menu_bar_spacer)

        self.bt_min = QPushButton(self.menu_bar)
        self.bt_min.setObjectName(u"bt_min")
        self.bt_min.setMinimumSize(QSize(35, 35))
        self.bt_min.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"Media/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_min.setIcon(icon1)
        self.bt_min.setIconSize(QSize(32, 32))
        self.bt_min.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_min, 0, Qt.AlignRight)

        self.bt_restore = QPushButton(self.menu_bar)
        self.bt_restore.setObjectName(u"bt_restore")
        self.bt_restore.setMaximumSize(QSize(35, 35))
        self.bt_restore.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u"Media/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restore.setIcon(icon2)
        self.bt_restore.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.bt_restore, 0, Qt.AlignRight)

        self.bt_max = QPushButton(self.menu_bar)
        self.bt_max.setObjectName(u"bt_max")
        self.bt_max.setMaximumSize(QSize(35, 35))
        self.bt_max.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u"Media/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_max.setIcon(icon3)
        self.bt_max.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_max, 0, Qt.AlignRight)

        self.bt_close = QPushButton(self.menu_bar)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMaximumSize(QSize(35, 16777215))
        self.bt_close.setStyleSheet(u"QPushButton{\n"
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
        icon4.addFile(u"Media/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon4)
        self.bt_close.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_close, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.menu_bar)

        self.main_panel = QFrame(self.user_main_panel)
        self.main_panel.setObjectName(u"main_panel")
        self.main_panel.setStyleSheet(u"")
        self.main_panel.setFrameShape(QFrame.StyledPanel)
        self.main_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_panel)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lateral_bt_container = QFrame(self.main_panel)
        self.lateral_bt_container.setObjectName(u"lateral_bt_container")
        self.lateral_bt_container.setMinimumSize(QSize(200, 0))
        self.lateral_bt_container.setMaximumSize(QSize(0, 16777215))
        self.lateral_bt_container.setLayoutDirection(Qt.LeftToRight)
        self.lateral_bt_container.setAutoFillBackground(False)
        self.lateral_bt_container.setStyleSheet(u"\n"
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
        self.lateral_bt_container.setFrameShape(QFrame.StyledPanel)
        self.lateral_bt_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.lateral_bt_container)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.bt_task_management = QPushButton(self.lateral_bt_container)
        self.bt_task_management.setObjectName(u"bt_task_management")
        self.bt_task_management.setMinimumSize(QSize(0, 40))
        self.bt_task_management.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_task_management.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"Media/taskC.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_task_management.setIcon(icon5)
        self.bt_task_management.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_task_management)

        self.bt_budget = QPushButton(self.lateral_bt_container)
        self.bt_budget.setObjectName(u"bt_budget")
        self.bt_budget.setMinimumSize(QSize(0, 40))
        self.bt_budget.setToolTipDuration(0)
        self.bt_budget.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"Media/budget.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_budget.setIcon(icon6)
        self.bt_budget.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_budget)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.vertical_spacer)

        self.bt_settings = QPushButton(self.lateral_bt_container)
        self.bt_settings.setObjectName(u"bt_settings")
        self.bt_settings.setMinimumSize(QSize(0, 40))
        self.bt_settings.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"Media/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_settings.setIcon(icon7)
        self.bt_settings.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_settings)

        self.bt_help = QPushButton(self.lateral_bt_container)
        self.bt_help.setObjectName(u"bt_help")
        self.bt_help.setMinimumSize(QSize(0, 40))
        self.bt_help.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"Media/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_help.setIcon(icon8)
        self.bt_help.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_help)

        self.bt_log_out = QPushButton(self.lateral_bt_container)
        self.bt_log_out.setObjectName(u"bt_log_out")
        self.bt_log_out.setMinimumSize(QSize(0, 40))
        self.bt_log_out.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"Media/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_log_out.setIcon(icon9)
        self.bt_log_out.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_log_out)


        self.horizontalLayout.addWidget(self.lateral_bt_container, 0, Qt.AlignLeft)

        self.central_card_container = QStackedWidget(self.main_panel)
        self.central_card_container.setObjectName(u"central_card_container")
        self.central_card_container.setMinimumSize(QSize(0, 0))
        self.central_card_container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.central_card_container.setFrameShape(QFrame.NoFrame)
        self.central_card_container.setFrameShadow(QFrame.Plain)
        self.central_card_container.setLineWidth(0)
        self.task_card = QWidget()
        self.task_card.setObjectName(u"task_card")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_card.sizePolicy().hasHeightForWidth())
        self.task_card.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.task_card)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.task_panel = QWidget(self.task_card)
        self.task_panel.setObjectName(u"task_panel")
        self.verticalLayout_22 = QVBoxLayout(self.task_panel)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.task_frame = QFrame(self.task_panel)
        self.task_frame.setObjectName(u"task_frame")
        self.task_frame.setFrameShape(QFrame.StyledPanel)
        self.task_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.task_frame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.task_management_main_title = QLabel(self.task_frame)
        self.task_management_main_title.setObjectName(u"task_management_main_title")
        self.task_management_main_title.setStyleSheet(u"font: 87 15pt \"Arial Black\";")
        self.task_management_main_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.task_management_main_title)

        self.task_option_container = QWidget(self.task_frame)
        self.task_option_container.setObjectName(u"task_option_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(20)
        sizePolicy1.setHeightForWidth(self.task_option_container.sizePolicy().hasHeightForWidth())
        self.task_option_container.setSizePolicy(sizePolicy1)
        self.task_option_container.setStyleSheet(u"QPushButton{\n"
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
        self.verticalLayout_20 = QVBoxLayout(self.task_option_container)
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.task_spacer_above = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_20.addItem(self.task_spacer_above)

        self.task_option_hor_layout = QHBoxLayout()
        self.task_option_hor_layout.setObjectName(u"task_option_hor_layout")
        self.task_option_hor_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.task_search_list = QPushButton(self.task_option_container)
        self.task_search_list.setObjectName(u"task_search_list")
        self.task_search_list.setIconSize(QSize(20, 20))

        self.task_option_hor_layout.addWidget(self.task_search_list)

        self.task_edit_list = QPushButton(self.task_option_container)
        self.task_edit_list.setObjectName(u"task_edit_list")

        self.task_option_hor_layout.addWidget(self.task_edit_list)


        self.verticalLayout_20.addLayout(self.task_option_hor_layout)

        self.task_spacer_below = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_20.addItem(self.task_spacer_below)


        self.verticalLayout_19.addWidget(self.task_option_container)

        self.task_table_container = QWidget(self.task_frame)
        self.task_table_container.setObjectName(u"task_table_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(150)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.task_table_container.sizePolicy().hasHeightForWidth())
        self.task_table_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_21 = QVBoxLayout(self.task_table_container)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.task_table = QTableWidget(self.task_table_container)
        if (self.task_table.columnCount() < 4):
            self.task_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.task_table.rowCount() < 3):
            self.task_table.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.task_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.task_table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.task_table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.task_table.setObjectName(u"task_table")

        self.verticalLayout_21.addWidget(self.task_table)


        self.verticalLayout_19.addWidget(self.task_table_container)


        self.verticalLayout_22.addWidget(self.task_frame)


        self.verticalLayout_9.addWidget(self.task_panel)

        self.central_card_container.addWidget(self.task_card)
        self.budget_card = QWidget()
        self.budget_card.setObjectName(u"budget_card")
        sizePolicy.setHeightForWidth(self.budget_card.sizePolicy().hasHeightForWidth())
        self.budget_card.setSizePolicy(sizePolicy)
        self.budget_card.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.budget_card)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.budget_panel = QWidget(self.budget_card)
        self.budget_panel.setObjectName(u"budget_panel")
        self.verticalLayout_17 = QVBoxLayout(self.budget_panel)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.budget_frame = QFrame(self.budget_panel)
        self.budget_frame.setObjectName(u"budget_frame")
        self.budget_frame.setFrameShape(QFrame.StyledPanel)
        self.budget_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.budget_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.budget_main_title = QLabel(self.budget_frame)
        self.budget_main_title.setObjectName(u"budget_main_title")
        self.budget_main_title.setLayoutDirection(Qt.LeftToRight)
        self.budget_main_title.setStyleSheet(u"font: 87 15pt \"Arial Black\";\n"
"")
        self.budget_main_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.budget_main_title)

        self.budget_spacer_above = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.budget_spacer_above)

        self.budget_option_container = QWidget(self.budget_frame)
        self.budget_option_container.setObjectName(u"budget_option_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.budget_option_container.sizePolicy().hasHeightForWidth())
        self.budget_option_container.setSizePolicy(sizePolicy3)
        self.budget_option_container.setStyleSheet(u"QPushButton{\n"
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
        self.horizontalLayout_3 = QHBoxLayout(self.budget_option_container)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.budget_option_container_hor_layout = QHBoxLayout()
        self.budget_option_container_hor_layout.setObjectName(u"budget_option_container_hor_layout")
        self.budget_option_container_hor_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.budget_search_list = QPushButton(self.budget_option_container)
        self.budget_search_list.setObjectName(u"budget_search_list")

        self.budget_option_container_hor_layout.addWidget(self.budget_search_list)

        self.budget_edit_list = QPushButton(self.budget_option_container)
        self.budget_edit_list.setObjectName(u"budget_edit_list")

        self.budget_option_container_hor_layout.addWidget(self.budget_edit_list)


        self.horizontalLayout_3.addLayout(self.budget_option_container_hor_layout)


        self.verticalLayout_16.addWidget(self.budget_option_container)

        self.budget_spacer_below = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.budget_spacer_below)

        self.budget_table_container = QWidget(self.budget_frame)
        self.budget_table_container.setObjectName(u"budget_table_container")
        sizePolicy2.setHeightForWidth(self.budget_table_container.sizePolicy().hasHeightForWidth())
        self.budget_table_container.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.budget_table_container)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.budget_table = QTableWidget(self.budget_table_container)
        if (self.budget_table.columnCount() < 4):
            self.budget_table.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.budget_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.budget_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.budget_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.budget_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        if (self.budget_table.rowCount() < 4):
            self.budget_table.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.budget_table.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.budget_table.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.budget_table.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.budget_table.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.budget_table.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.budget_table.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.budget_table.setItem(0, 3, __qtablewidgetitem17)
        self.budget_table.setObjectName(u"budget_table")
        sizePolicy3.setHeightForWidth(self.budget_table.sizePolicy().hasHeightForWidth())
        self.budget_table.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.budget_table)


        self.verticalLayout_16.addWidget(self.budget_table_container)


        self.verticalLayout_17.addWidget(self.budget_frame)


        self.verticalLayout_4.addWidget(self.budget_panel)

        self.central_card_container.addWidget(self.budget_card)
        self.settings_card = QWidget()
        self.settings_card.setObjectName(u"settings_card")
        sizePolicy.setHeightForWidth(self.settings_card.sizePolicy().hasHeightForWidth())
        self.settings_card.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.settings_card)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.settings_panel = QWidget(self.settings_card)
        self.settings_panel.setObjectName(u"settings_panel")
        self.verticalLayout_13 = QVBoxLayout(self.settings_panel)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.settings_main_title = QLabel(self.settings_panel)
        self.settings_main_title.setObjectName(u"settings_main_title")
        self.settings_main_title.setStyleSheet(u"font: 87 27pt \"Arial Black\";")

        self.verticalLayout_13.addWidget(self.settings_main_title)

        self.settings_email_container = QWidget(self.settings_panel)
        self.settings_email_container.setObjectName(u"settings_email_container")
        self.verticalLayout_10 = QVBoxLayout(self.settings_email_container)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.settings_email_label = QLabel(self.settings_email_container)
        self.settings_email_label.setObjectName(u"settings_email_label")
        self.settings_email_label.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_10.addWidget(self.settings_email_label)

        self.settings_email_textfield = QLineEdit(self.settings_email_container)
        self.settings_email_textfield.setObjectName(u"settings_email_textfield")
        self.settings_email_textfield.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.settings_email_textfield)


        self.verticalLayout_13.addWidget(self.settings_email_container)

        self.settings_phone_container = QWidget(self.settings_panel)
        self.settings_phone_container.setObjectName(u"settings_phone_container")
        self.verticalLayout_11 = QVBoxLayout(self.settings_phone_container)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.settings_phone_label = QLabel(self.settings_phone_container)
        self.settings_phone_label.setObjectName(u"settings_phone_label")
        self.settings_phone_label.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_11.addWidget(self.settings_phone_label)

        self.settings_phone_textfield = QLineEdit(self.settings_phone_container)
        self.settings_phone_textfield.setObjectName(u"settings_phone_textfield")
        self.settings_phone_textfield.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.settings_phone_textfield)


        self.verticalLayout_13.addWidget(self.settings_phone_container)

        self.settings_addr_container = QWidget(self.settings_panel)
        self.settings_addr_container.setObjectName(u"settings_addr_container")
        self.verticalLayout_12 = QVBoxLayout(self.settings_addr_container)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.settings_addr_label = QLabel(self.settings_addr_container)
        self.settings_addr_label.setObjectName(u"settings_addr_label")
        self.settings_addr_label.setStyleSheet(u"font: 87 15pt \"Arial Black\";")

        self.verticalLayout_12.addWidget(self.settings_addr_label)

        self.settings_addr_textfield = QLineEdit(self.settings_addr_container)
        self.settings_addr_textfield.setObjectName(u"settings_addr_textfield")
        self.settings_addr_textfield.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.settings_addr_textfield)


        self.verticalLayout_13.addWidget(self.settings_addr_container)

        self.settings_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.settings_spacer)


        self.verticalLayout_6.addWidget(self.settings_panel)

        self.central_card_container.addWidget(self.settings_card)
        self.help_card = QWidget()
        self.help_card.setObjectName(u"help_card")
        sizePolicy.setHeightForWidth(self.help_card.sizePolicy().hasHeightForWidth())
        self.help_card.setSizePolicy(sizePolicy)
        self.help_card.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QVBoxLayout(self.help_card)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.help_panel = QWidget(self.help_card)
        self.help_panel.setObjectName(u"help_panel")
        self.verticalLayout_15 = QVBoxLayout(self.help_panel)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.help_main_title = QLabel(self.help_panel)
        self.help_main_title.setObjectName(u"help_main_title")
        self.help_main_title.setStyleSheet(u"font: 87 25pt \"Arial Black\";")

        self.verticalLayout_15.addWidget(self.help_main_title)

        self.help_ask_container = QWidget(self.help_panel)
        self.help_ask_container.setObjectName(u"help_ask_container")
        self.verticalLayout_14 = QVBoxLayout(self.help_ask_container)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.help_ask_label = QLabel(self.help_ask_container)
        self.help_ask_label.setObjectName(u"help_ask_label")
        self.help_ask_label.setStyleSheet(u"font: 87 14pt \"Arial Black\";")

        self.verticalLayout_14.addWidget(self.help_ask_label)

        self.help_ask_textbox = QTextEdit(self.help_ask_container)
        self.help_ask_textbox.setObjectName(u"help_ask_textbox")

        self.verticalLayout_14.addWidget(self.help_ask_textbox)


        self.verticalLayout_15.addWidget(self.help_ask_container)

        self.help_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.help_spacer)


        self.verticalLayout_7.addWidget(self.help_panel)

        self.central_card_container.addWidget(self.help_card)
        self.log_out_card = QWidget()
        self.log_out_card.setObjectName(u"log_out_card")
        self.widget = QWidget(self.log_out_card)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, -1, 601, 571))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton)

        self.central_card_container.addWidget(self.log_out_card)

        self.horizontalLayout.addWidget(self.central_card_container)


        self.verticalLayout.addWidget(self.main_panel)

        UserMainWindow.setCentralWidget(self.user_main_panel)

        self.retranslateUi(UserMainWindow)

        self.bt_menu.setDefault(False)
        self.central_card_container.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(UserMainWindow)
    # setupUi

    def retranslateUi(self, UserMainWindow):
        UserMainWindow.setWindowTitle(QCoreApplication.translate("UserMainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("UserMainWindow", u"Menu", None))
        self.bt_min.setText("")
        self.bt_restore.setText("")
        self.bt_max.setText("")
        self.bt_close.setText("")
        self.bt_task_management.setText(QCoreApplication.translate("UserMainWindow", u"Task Management", None))
        self.bt_budget.setText(QCoreApplication.translate("UserMainWindow", u"Budget Management", None))
        self.bt_settings.setText(QCoreApplication.translate("UserMainWindow", u"Settings", None))
        self.bt_help.setText(QCoreApplication.translate("UserMainWindow", u"Help", None))
        self.bt_log_out.setText(QCoreApplication.translate("UserMainWindow", u"Log Out", None))
        self.task_management_main_title.setText(QCoreApplication.translate("UserMainWindow", u"Task Management", None))
        self.task_search_list.setText(QCoreApplication.translate("UserMainWindow", u"Search List", None))
        self.task_edit_list.setText(QCoreApplication.translate("UserMainWindow", u"EditList", None))
        ___qtablewidgetitem = self.task_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UserMainWindow", u"Estimated minimun", None));
        ___qtablewidgetitem1 = self.task_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UserMainWindow", u"Estimated maximun", None));
        ___qtablewidgetitem2 = self.task_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UserMainWindow", u"Estimated time", None));
        ___qtablewidgetitem3 = self.task_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UserMainWindow", u"Time", None));
        ___qtablewidgetitem4 = self.task_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("UserMainWindow", u"Nouvelle ligne", None));
        ___qtablewidgetitem5 = self.task_table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("UserMainWindow", u"Task1", None));
        ___qtablewidgetitem6 = self.task_table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("UserMainWindow", u"Task3", None));
        self.budget_main_title.setText(QCoreApplication.translate("UserMainWindow", u"Budget Management", None))
        self.budget_search_list.setText(QCoreApplication.translate("UserMainWindow", u"Search List", None))
        self.budget_edit_list.setText(QCoreApplication.translate("UserMainWindow", u"EditList", None))
        ___qtablewidgetitem7 = self.budget_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("UserMainWindow", u"Estimated minimun", None));
        ___qtablewidgetitem8 = self.budget_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("UserMainWindow", u"Estimated maximun", None));
        ___qtablewidgetitem9 = self.budget_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("UserMainWindow", u"Estimated time", None));
        ___qtablewidgetitem10 = self.budget_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("UserMainWindow", u"Time", None));
        ___qtablewidgetitem11 = self.budget_table.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("UserMainWindow", u"Bugdet1", None));
        ___qtablewidgetitem12 = self.budget_table.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("UserMainWindow", u"Budget2", None));
        ___qtablewidgetitem13 = self.budget_table.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("UserMainWindow", u"Bugdet3", None));
        ___qtablewidgetitem14 = self.budget_table.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("UserMainWindow", u"Budget4", None));

        __sortingEnabled = self.budget_table.isSortingEnabled()
        self.budget_table.setSortingEnabled(False)
        self.budget_table.setSortingEnabled(__sortingEnabled)

        self.settings_main_title.setText(QCoreApplication.translate("UserMainWindow", u"Account Settings", None))
        self.settings_email_label.setText(QCoreApplication.translate("UserMainWindow", u"Email Address", None))
        self.settings_email_textfield.setText(QCoreApplication.translate("UserMainWindow", u"example@gmail.com", None))
        self.settings_phone_label.setText(QCoreApplication.translate("UserMainWindow", u"Phone Number", None))
        self.settings_phone_textfield.setText(QCoreApplication.translate("UserMainWindow", u"672154987", None))
        self.settings_addr_label.setText(QCoreApplication.translate("UserMainWindow", u"Address", None))
        self.settings_addr_textfield.setText("")
        self.help_main_title.setText(QCoreApplication.translate("UserMainWindow", u"Welcome to help page", None))
        self.help_ask_label.setText(QCoreApplication.translate("UserMainWindow", u"Ask us something, we\u00b4ll respond via Email", None))
        self.pushButton.setText(QCoreApplication.translate("UserMainWindow", u"Log out", None))
    # retranslateUi

