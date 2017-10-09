# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.message_list = QtWidgets.QListView(self.centralwidget)
        self.message_list.setGeometry(QtCore.QRect(0, 0, 641, 541))
        self.message_list.setObjectName("message_list")
        self.message_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_edit.setGeometry(QtCore.QRect(0, 560, 551, 41))
        self.message_edit.setObjectName("message_edit")
        self.Button_send = QtWidgets.QPushButton(self.centralwidget)
        self.Button_send.setGeometry(QtCore.QRect(560, 560, 81, 41))
        self.Button_send.setObjectName("Button_send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_send.setText(_translate("MainWindow", "Send"))

