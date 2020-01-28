import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully Socket Created !")
except socket.error as err:
    print("Socket Creation Error : " + err)

port = 80


try:
    host = socket.gethostbyname("www.google.co.in")
except socket.gaierror as err:
    print("Socket to Server Connection Error : " + err)
    sys.exit()

sock.connect((host, port))
print("The socket has been created on :" + str(host) + ' and ' + str(port))