host = input("hostname:")
port = input("port:")
heim = server(host, port)
heim.connect()
rep = heim.send("coucou")
    if rep =="":
        print("serveur non connecté")
    else:
        print(rep)