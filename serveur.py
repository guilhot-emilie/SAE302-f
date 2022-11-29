import socket

class serveur:
    def __init__(self, hostname, port)
        self.__port = port
        self.__hostname = hostname
        self.__socket = None

    def isConnected(self):
        return(self.__socket!=None)

    def __Connected(self):
        socket = socket.socket()
        socket.connect(self.__host,self.__port)

    def __send(self,msg):
        if self.isConnected():
            socket.send(msg)
            msg=socket.receive(._)
            print(msg)
        else:
            print("Pas de connexion")

def close(self):
    socket.close()

