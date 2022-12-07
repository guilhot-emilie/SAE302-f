import socket

port = 4004

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

# Réception du message du client
msgb = conn.recv(1024) # message en by
message = msgb.decode()
print(f"Message du client : {message}")

# J'envoie un message
reply = input("Saisir un message : ")
conn.send(reply.encode())
print(f"Message {reply} envoyé")

# Fermeture
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")