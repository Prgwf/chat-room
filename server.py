# -*- coding: utf-8 -*-
import socket, threading, sys, re, time

default_host = '127.0.0.1'
default_port = 8989

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((default_host, default_port))
server_socket.listen(10)

def broadcast(message):
    pass

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    conn, addr = server_socket.accept()
    t = threading.Thread(target = tcplink, args = (conn, addr))
    t.start()
