# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 718)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.xButtom = QPushButton(self.centralwidget)
        self.xButtom.setObjectName(u"xButtom")
        self.xButtom.setMaximumSize(QSize(30, 30))
        self.xButtom.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.xButtom)

        self.edit_buttom = QPushButton(self.centralwidget)
        self.edit_buttom.setObjectName(u"edit_buttom")
        self.edit_buttom.setMaximumSize(QSize(30, 30))
        self.edit_buttom.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit_buttom)

        self.text_buttom = QPushButton(self.centralwidget)
        self.text_buttom.setObjectName(u"text_buttom")
        self.text_buttom.setMaximumSize(QSize(30, 30))
        self.text_buttom.setCheckable(False)

        self.horizontalLayout.addWidget(self.text_buttom)

        self.play_buttom = QPushButton(self.centralwidget)
        self.play_buttom.setObjectName(u"play_buttom")
        self.play_buttom.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.play_buttom)

        self.useCameraButtom = QPushButton(self.centralwidget)
        self.useCameraButtom.setObjectName(u"useCameraButtom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.useCameraButtom.sizePolicy().hasHeightForWidth())
        self.useCameraButtom.setSizePolicy(sizePolicy1)
        self.useCameraButtom.setLayoutDirection(Qt.LeftToRight)
        self.useCameraButtom.setCheckable(True)

        self.horizontalLayout.addWidget(self.useCameraButtom)

        self.captureButton = QPushButton(self.centralwidget)
        self.captureButton.setObjectName(u"captureButton")
        sizePolicy1.setHeightForWidth(self.captureButton.sizePolicy().hasHeightForWidth())
        self.captureButton.setSizePolicy(sizePolicy1)
        self.captureButton.setLayoutDirection(Qt.LeftToRight)
        self.captureButton.setCheckable(True)
        self.captureButton.setChecked(True)

        self.horizontalLayout.addWidget(self.captureButton)

        self.detect_buttom = QPushButton(self.centralwidget)
        self.detect_buttom.setObjectName(u"detect_buttom")
        sizePolicy1.setHeightForWidth(self.detect_buttom.sizePolicy().hasHeightForWidth())
        self.detect_buttom.setSizePolicy(sizePolicy1)
        self.detect_buttom.setLayoutDirection(Qt.LeftToRight)
        self.detect_buttom.setCheckable(True)

        self.horizontalLayout.addWidget(self.detect_buttom)

        self.pdf_buttom = QPushButton(self.centralwidget)
        self.pdf_buttom.setObjectName(u"pdf_buttom")

        self.horizontalLayout.addWidget(self.pdf_buttom)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.right_buttom = QPushButton(self.centralwidget)
        self.right_buttom.setObjectName(u"right_buttom")
        self.right_buttom.setMaximumSize(QSize(30, 50))

        self.horizontalLayout_2.addWidget(self.right_buttom, 0, Qt.AlignRight)

        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy2)
        self.imageFrame.setMinimumSize(QSize(800, 600))
        self.imageFrame.setSizeIncrement(QSize(0, 0))
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.imageFrame)

        self.left_buttom = QPushButton(self.centralwidget)
        self.left_buttom.setObjectName(u"left_buttom")
        self.left_buttom.setMaximumSize(QSize(30, 50))

        self.horizontalLayout_2.addWidget(self.left_buttom)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)
        self.spinBox.setMinimumSize(QSize(55, 0))
        self.spinBox.setLayoutDirection(Qt.LeftToRight)
        self.spinBox.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.spinBox, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.xButtom.setText("")
        self.edit_buttom.setText("")
        self.text_buttom.setText("")
        self.play_buttom.setText("")
        self.useCameraButtom.setText(QCoreApplication.translate("MainWindow", u"Use camera", None))
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"Stop capture", None))
        self.detect_buttom.setText(QCoreApplication.translate("MainWindow", u"Detect face", None))
        self.pdf_buttom.setText(QCoreApplication.translate("MainWindow", u"Load PDF", None))
        self.right_buttom.setText("")
        self.left_buttom.setText("")
    # retranslateUi

