#author: Chris Nelson

import socket
import os
import random

#local host and port 
local_host = socket.gethostname()
port = 24555
print("server running and listening on port", port)

#set up socket and bind
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_host, port))

#listen with a backlog of 5
server.listen(5)
(client, address) = server.accept()
print("server connected to host:", address)

while 1:
    #this is a blocking call, waiting for accept.  As it stands, this program cannot
    #handle multiple calls, this is a one and done test program.

    #print and send data
    size = client.recv(3)
    size = int(size.decode())

    data = client.recv(size)
    if data.decode() == 'exit':
        print("partner has ended the chat")
        break

    print(data.decode())
    data = input('::')

    #append the length string to the first (3) chars of the message
    mod_data = ""
    if len(data) < 10:
        mod_data+="00"
    elif len(data) < 100:
        mod_data+="0"
    elif len(data) > 999:
        print("message too large, must be < 1000 characters")
        continue

    #concat the len to the data
    mod_data += str(len(data))

    #add the message after the length
    mod_data += data

    client.send(mod_data.encode())
    if data == 'exit':
        break;

#close the connection
client.close()
