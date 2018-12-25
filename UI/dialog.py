# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.info = QtWidgets.QLineEdit(Dialog)
        self.info.setGeometry(QtCore.QRect(32, 100, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.info.setFont(font)
        self.info.setText("")
        self.info.setReadOnly(False)
        self.info.setObjectName("info")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(190, 230, 75, 23))
        self.confirm_button.setObjectName("confirm_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.value = QtWidgets.QSpinBox(Dialog)
        self.value.setGeometry(QtCore.QRect(90, 170, 42, 22))
        self.value.setObjectName("value")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.confirm_button.setText(_translate("Dialog", "确认"))
        self.cancel_button.setText(_translate("Dialog", "取消"))

