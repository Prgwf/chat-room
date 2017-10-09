import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 8989

class Server(object):
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.socket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((HOST, PORT))
        self.server.listen(100)
        self.list_of_clients = []
        self.user_info = {}

    def accept(self):
        conn, addr = self.server.accept()
        return conn, addr

    def verify(self, conn):
        time.sleep(0.5)
        user = conn.recv(1024).decode('utf-8').strip()
        time.sleep(0.5)
        passwd = conn.recv(1024).decode('utf-8')

        if user not in self.user_info.keys():
            time.sleep(0.5)
            conn.send(bytes('error: no such user!', 'utf-8'))
            conn.close()
            return None

        elif passwd != self.user_info[user]['passwd']:
            time.sleep(0.5)
            conn.send(bytes('error: wrong user or passwd!'), 'utf-8')
            conn.close()
            return None

        elif self.user_info[user]['online']:
            time.sleep(0.5)
            conn.send(bytes('error: %s is online' % user))
            conn.close()
            return None

        else:
            time.sleep(0.5)
            conn.send(bytes('%s is comming' % user))
            self.user_info[user]['socket'] = conn
            self.user_info[user]['online'] = True
            return user

    def broadcast(self, user, msg):
        pass

    def
if __name__ == '__main__':
    S = Server()
    global cont
    cont = 0

    while True:
        cont += 1
        time.sleep(3)
        conn, addr = S.accept()
        user = S.verify(conn)

        if user is not None and user in S.user_info.keys() and S.user_info[user]['online']:
            new_thread = threading.Thread(target = S.tran, args = (conn, addr))
            new_thread.start()