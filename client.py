import socket

class server:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = None

    def isConnected(self):
        return(self.__socket!=None)

    def Connected(self):
        socket = socket.socket()
        socket.connect(self.__host,self.__port)

    def Send(self,msg):
        if self.isConnected():
            socket.send(msg)
            msg=socket.receive(1024).decode()
            print(msg)
        else:
            print("Pas de connexion")

    def Close(self):
        socket.close()