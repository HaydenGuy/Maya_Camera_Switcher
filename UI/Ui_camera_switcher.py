# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_switcher.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_camera_switcher(object):
    def setupUi(self, camera_switcher):
        if not camera_switcher.objectName():
            camera_switcher.setObjectName(u"camera_switcher")
        camera_switcher.resize(261, 207)
        self.centralwidget = QWidget(camera_switcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_layout = QVBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.persp_bt = QPushButton(self.centralwidget)
        self.persp_bt.setObjectName(u"persp_bt")

        self.button_layout.addWidget(self.persp_bt)

        self.top_bt = QPushButton(self.centralwidget)
        self.top_bt.setObjectName(u"top_bt")

        self.button_layout.addWidget(self.top_bt)

        self.front_bt = QPushButton(self.centralwidget)
        self.front_bt.setObjectName(u"front_bt")

        self.button_layout.addWidget(self.front_bt)

        self.side_bt = QPushButton(self.centralwidget)
        self.side_bt.setObjectName(u"side_bt")

        self.button_layout.addWidget(self.side_bt)


        self.horizontalLayout.addLayout(self.button_layout)

        camera_switcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(camera_switcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 261, 23))
        camera_switcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(camera_switcher)
        self.statusbar.setObjectName(u"statusbar")
        camera_switcher.setStatusBar(self.statusbar)

        self.retranslateUi(camera_switcher)

        QMetaObject.connectSlotsByName(camera_switcher)
    # setupUi

    def retranslateUi(self, camera_switcher):
        camera_switcher.setWindowTitle(QCoreApplication.translate("camera_switcher", u"Camera Switcher", None))
        self.persp_bt.setText(QCoreApplication.translate("camera_switcher", u"persp", None))
        self.top_bt.setText(QCoreApplication.translate("camera_switcher", u"top", None))
        self.front_bt.setText(QCoreApplication.translate("camera_switcher", u"front", None))
        self.side_bt.setText(QCoreApplication.translate("camera_switcher", u"side", None))
    # retranslateUi

