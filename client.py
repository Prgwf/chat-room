import socket,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from login import Ui_Dialog
from main import Ui_MainWindow

class Client(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.login_window = Ui_Dialog()
        self.login_window.Button_login.clicked.connect(self.login_button)
        self.login_window.Button_register.clicked.connect(self.register_button)
        self.main_window = Ui_MainWindow()
        self.main_window.Button_send.clicked.connect(self.send_button)

    def login_button(self):
        pass

    def register_button(self):
        pass

    def send_button(self):
        pass

    def login(self):
        pass

    def register(self):
        pass


if __name__ == '__main__':
    window = Client()
    window.login_window.show()
    sys.exit(window.app.exec_())