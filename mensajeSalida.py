# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 184)
        self.imagen = QLabel(Form)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setGeometry(QRect(40, 60, 70, 70))
        self.texto = QLabel(Form)
        self.texto.setObjectName(u"texto")
        self.texto.setGeometry(QRect(170, 60, 191, 70))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imagen.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.texto.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

