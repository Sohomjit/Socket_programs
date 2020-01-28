import socket

sock = socket.socket()
print("Socket has been successfully created !")

port = 55555

sock.bind(('', port))
print("Socket has been binded to : " + str(port))

sock.listen(5)
print("Socket is now listening !")

while True:

    sock, client_address = sock.accept()
    print("Connected to " + str(client_address))

    sock.send("Thank you for connecting :-) ")

    sock.close() 