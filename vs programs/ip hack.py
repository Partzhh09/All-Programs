import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket sucessfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

port = 80

try:
    host_ip = socket.gethostbyname('www.Youtube.com')
except socket.gaierror:

    print("There was error resolving the host")
    sys.exit()

s.connect((host_ip,port))

print("The socket successfully connected to google \ on port == %s" %(host_ip))