# -*- coding: utf-8 -*-
import sys, time, socket, threading
from ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore

server_host = '127.0.0.1'
server_port = 8989

class Client(object):
    def __init__(self):
        self.App = QtWidgets.QApplication(sys.argv)
        self.Window = Ui_MainWindow()
        self.Window.sendbutton.clicked.connect(self.send_button)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server_host, server_port))
        self.message_recv()

    def send_button(self):
        try:
            self.name = self.Window.namejar.text().strip()
            self.message = self.Window.msgjar.text()
            if self.name == '':
                QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), 'error', 'please input nickname')
                return
            elif self.message == '':
                QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), 'error', 'please input your message')
                return

            self.socket.send(bytes(self.name + '|' + self.message, 'utf-8'))
            self.Window.msgjar.setText('')
        except BaseException as err:
            QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), 'error', str(err))

    def message_recv(self):
        def recv_help():
            model = QtGui.QStandardItemModel(self.Window.msglist)
            while True:
                try:
                    msg = self.socket.recv(2048).decode('utf-8')
                    t = time.strftime('%Y-%m-%d %H:%M:%S\t', time.localtime())
                    msg = t + ' ' + msg
                    raw = QtGui.QStandardItem()
                    raw.setText(msg)
                    model.appendRow(raw)
                    self.Window.msglist.setModel(model)
                    self.Window.msglist.update()
                except socket.error:
                    break
        sub_thread = threading.Thread(target=recv_help, args=())
        sub_thread.setDaemon(True)
        sub_thread.start()

if __name__ == '__main__':
    t = Client()
    t.Window.show()
    sys.exit(t.App.exec_())