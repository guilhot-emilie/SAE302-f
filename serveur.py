import socket

host = "localhost" # "", "127.0.0.1
port = 10000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
msgserv = msg = ""
print('En attente du client')
while msg !="arret" and msgserv !="arret":
    conn, address = server_socket.accept()
    print(f'Client connecté {address}')
    msgserv = msg = ""
    while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
        # Réception du message du client
        msgb = conn.recv(1024) # message en by
        msg = msgb.decode()
        print(f"Message du client : {msg}")
        if msgb =="bye":
            conn.send("bye".encode())
        else:
            # J'envoie un message
            msgserv = input("Saisir un message : ")
            conn.send(reply.encode())
            print(f"Message {msgserv} envoyé")
    # Fermeture
    conn.close()
    print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")