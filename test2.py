import socket
from client import server
#import serveur


host = input("hostname:")
port = input("port:")
heim = server(host, port)
heim.Connected()
rep = heim.Send("coucou")
if rep =="":
    print("serveur non connecté")
else:
    print(rep)