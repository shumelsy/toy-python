#!/usr/bin/python2

import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0:
        data = conn.recv(1024)
        if data == 'close': break
        conn.send(data)
    conn.close()


