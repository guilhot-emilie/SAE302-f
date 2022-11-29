import socket

host = "localhost" # "", "127.0.0.1
port = 10000

#Connexion au serveur
print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")
msgserv = msg = ""
while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
    #Envoie message
    msg = input("Message au serveur : ")
    client_socket.send(msg.encode())
    print("Message envoyé")

    #Reception message
    msgserv = client_socket.recv(1024).decode()
    print(f"Message du serveur : {msgserv}")

# Fermeture de la socket du client
client_socket.close()
print("Socket fermée")