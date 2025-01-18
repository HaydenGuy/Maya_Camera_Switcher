# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_switcher.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_camera_switcher(object):
    def setupUi(self, camera_switcher):
        if not camera_switcher.objectName():
            camera_switcher.setObjectName(u"camera_switcher")
        camera_switcher.resize(238, 206)
        self.action_create_camera = QAction(camera_switcher)
        self.action_create_camera.setObjectName(u"action_create_camera")
        self.centralwidget = QWidget(camera_switcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 220, 142))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_layout = QVBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.persp_bt = QPushButton(self.scrollAreaWidgetContents)
        self.persp_bt.setObjectName(u"persp_bt")

        self.button_layout.addWidget(self.persp_bt)

        self.top_bt = QPushButton(self.scrollAreaWidgetContents)
        self.top_bt.setObjectName(u"top_bt")

        self.button_layout.addWidget(self.top_bt)

        self.front_bt = QPushButton(self.scrollAreaWidgetContents)
        self.front_bt.setObjectName(u"front_bt")

        self.button_layout.addWidget(self.front_bt)

        self.side_bt = QPushButton(self.scrollAreaWidgetContents)
        self.side_bt.setObjectName(u"side_bt")

        self.button_layout.addWidget(self.side_bt)


        self.horizontalLayout_2.addLayout(self.button_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        camera_switcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(camera_switcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 238, 23))
        self.create_menu_bar = QMenu(self.menubar)
        self.create_menu_bar.setObjectName(u"create_menu_bar")
        camera_switcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(camera_switcher)
        self.statusbar.setObjectName(u"statusbar")
        camera_switcher.setStatusBar(self.statusbar)

        self.menubar.addAction(self.create_menu_bar.menuAction())
        self.create_menu_bar.addAction(self.action_create_camera)

        self.retranslateUi(camera_switcher)

        QMetaObject.connectSlotsByName(camera_switcher)
    # setupUi

    def retranslateUi(self, camera_switcher):
        camera_switcher.setWindowTitle(QCoreApplication.translate("camera_switcher", u"Camera Switcher", None))
        self.action_create_camera.setText(QCoreApplication.translate("camera_switcher", u"Camera", None))
        self.persp_bt.setText(QCoreApplication.translate("camera_switcher", u"persp", None))
        self.top_bt.setText(QCoreApplication.translate("camera_switcher", u"top", None))
        self.front_bt.setText(QCoreApplication.translate("camera_switcher", u"front", None))
        self.side_bt.setText(QCoreApplication.translate("camera_switcher", u"side", None))
        self.create_menu_bar.setTitle(QCoreApplication.translate("camera_switcher", u"Create...", None))
    # retranslateUi

