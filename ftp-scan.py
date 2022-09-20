#!/usr/bin/python

import socket
import sys

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],21))

print (b"Conectando ao servidor...")
banner = tcp.recv(1024)
print (banner)

print (b"Enviando usuario...")
tcp.send(b"USER anonymous\r\n")
user = tcp.recv(1024)
print (user)

print (b"Enviando a senha...")
tcp.send(b"PASS\r\n")
pw = tcp.recv(1024)
print (pw)

print (b"Enviando comando HELP...")
tcp.send(b"dir \r\n")
cmd = tcp.recv(2048)
print (cmd)