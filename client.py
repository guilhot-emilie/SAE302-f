import socket

class server:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = None

    def Connected(self):
        self.__socket = socket.socket()
        self.__socket.connect((self.__host,self.__port))

    def isConnected(self):
        return(self.__socket!=None)

    def send(self,msg):
        if self.isConnected():
            self.__socket.send(msg.encode())
            msg=self.__socket.recv(1024).decode()
            print(msg)
        else:
            print("Pas de connexion")

    def Close(self):
        self.__socket.close()