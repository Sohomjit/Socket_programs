import socket

sock = socket.socket()

port = 55555

print('Socket trying to connect . . .')

sock.connect(('127.0.0.1', port))

print('connected . . .')

print (sock.recv(1024))

print('closing socket !')

sock.close()