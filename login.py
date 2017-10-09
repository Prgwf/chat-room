# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 311)
        self.Button_login = QtWidgets.QPushButton(Dialog)
        self.Button_login.setGeometry(QtCore.QRect(140, 160, 92, 36))
        self.Button_login.setObjectName("Button_login")
        self.lineEdit_passwd = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(140, 110, 201, 36))
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.Button_register = QtWidgets.QPushButton(Dialog)
        self.Button_register.setGeometry(QtCore.QRect(250, 160, 92, 36))
        self.Button_register.setObjectName("Button_register")
        self.label_user = QtWidgets.QLabel(Dialog)
        self.label_user.setGeometry(QtCore.QRect(80, 80, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.label_passwd = QtWidgets.QLabel(Dialog)
        self.label_passwd.setGeometry(QtCore.QRect(70, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_passwd.setFont(font)
        self.label_passwd.setObjectName("label_passwd")
        self.lineEdit_user = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_user.setGeometry(QtCore.QRect(140, 70, 201, 36))
        self.lineEdit_user.setObjectName("lineEdit_user")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_login.setText(_translate("Dialog", "login"))
        self.Button_register.setText(_translate("Dialog", "register"))
        self.label_user.setText(_translate("Dialog", "user"))
        self.label_passwd.setText(_translate("Dialog", "passwd"))

