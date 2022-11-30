import socket, threading

class server:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = None

    def __connected(self):
        self.__socket = socket.socket()
        self.__socket.connect((self.__host,self.__port))

    def isConnected(self):
        return(self.__socket!=None)

    def __send(self,msg):
        if self.isConnected():
            self.__socket.send(msg.encode())
            msg=self.__socket.recv(1024).decode()
            print(msg)
        else:
            print("Pas de connexion")

    def close(self):
        self.__socket.close()

    def connect(self):
        self.__tconnected = threading.Thread(target = self.__connect)
        self.__tconnected.start()


    def send(self):
        self.__tsend = threading.Thread(target = self.__send)
        self.__tsend.start()
        self.verrou = threading.Lock()
        self.verrou.acquire()
        self.verrou.release()