import socket
from client import serveur


host = input("hostname:")
port = input("port:")
heim = serveur(host, port)
heim.connect()
rep = heim.send("coucou")
if rep =="":
    print("serveur non connecté")
else:
    print(rep)