# -*- coding: utf-8 -*-
import sys, time, socket
from ui import Ui_MainWindow
from PyQt5 import QtWidgets

class Client(object):
    def __init__(self):
        self.App = QtWidgets.QApplication(sys.argv)
        self.Window = Ui_MainWindow()
        self.Window.sendbutton.clicked.connect(self.send_button)


    def send_button(self):
        pass

if __name__ == '__main__':
    t = Client()
    t.Window.show()
    sys.exit(t.App.exec_())