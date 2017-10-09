# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
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
        MainWindow.resize(850, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(20, 600, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")
        self.sendbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sendbutton.setGeometry(QtCore.QRect(10, 720, 92, 36))
        self.sendbutton.setObjectName("sendbutton")
        self.namejar = QtWidgets.QLineEdit(self.centralwidget)
        self.namejar.setGeometry(QtCore.QRect(10, 630, 113, 36))
        self.namejar.setObjectName("namejar")
        self.msgjar = QtWidgets.QLineEdit(self.centralwidget)
        self.msgjar.setGeometry(QtCore.QRect(10, 670, 791, 41))
        self.msgjar.setObjectName("msgjar")
        self.msglist = QtWidgets.QListView(self.centralwidget)
        self.msglist.setGeometry(QtCore.QRect(10, 20, 791, 571))
        self.msglist.setObjectName("msglist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatRoom"))
        self.namelabel.setText(_translate("MainWindow", "nickname"))
        self.sendbutton.setText(_translate("MainWindow", "Send"))

