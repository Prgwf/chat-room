# -*- coding: utf-8 -*-
import socket, threading, sys, re, time

default_host = '127.0.0.1'
default_port = 8989

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((default_host, default_port))
server_socket.listen(10)

client_list = []

def client_thread(conn, addr):
    while True:
        try:
            raw = conn.recv(2048)
            # debug why server no response
            # print(raw)
            if raw:
                raw = raw.decode('utf-8').split('|')
                message = '<' + raw[0] + '>: ' + raw[1]
                # print(raw[0], '\n', raw[1])
                broadcast(message, conn)
                conn.send(bytes('<You>: ' + raw[1], 'utf-8'))
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for client in client_list:
        if client != connection:
            try:
                client.send(bytes(message, 'utf-8'))
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection in client_list:
        client_list.remove(connection)


if __name__ == '__main__':
    while True:
        conn, addr = server_socket.accept()
        client_list.append(conn)
        t = threading.Thread(target = client_thread, args = (conn, addr))
        t.start()
