# coding: iso-8859-1 -*-
import socket
resp = "S"
while resp == "S":
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente a {} é {}".format(url, ip))
    resp = input("Digite <S> para continual: ").upper()
