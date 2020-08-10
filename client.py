#author: Chris Nelson
#simple chat app base written for experimenting w/ sockets and networking.  
#the default server port used is 24555, assume the client has the IP of the server.

import socket
import sys

host = socket.gethostname()

#must accept a socket(int) as argument
if len(sys.argv) != 2:
    print(errno)

#grab port from arg
port = int(sys.argv[1])

#set up client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to target socket on the web port of 80
client.connect((host, port))

#infinte loop until either server or client quits
while 1:
    data = input(':')

    #append the length string to the first (3) chars of the message
    mod_data = ""
    if len(data) < 10:
        mod_data+="00"
    elif len(data) < 100:
        mod_data+="0"
    elif len(data) > 999:
        print("message too large, must be < 1000 characters")
        continue

    #concat len 
    mod_data += str(len(data))

    #add the message after the length
    mod_data += data

    client.send(mod_data.encode())
    if data == 'exit':
        break

    #receive and determine size
    size = client.recv(3)
    size = int(size.decode())

    response = client.recv(size)
    if response.decode() == 'exit':
        print("pertner has ended the chat")
        break;

    print(response.decode())

client.close()
