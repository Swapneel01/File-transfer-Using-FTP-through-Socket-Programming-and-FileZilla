# server.py

import socket                   # Import socket module

port = 57272           # Reserve a port for your service.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             # Create a socket object #made changes here, added the parameters
# host = socket.gethostname()     # Get local machine name
host = "192.168.43.115"     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    # data = conn.recv(50000) #problems here check (1)
    # print('Server received', repr(data)) #changes made here, put eval after repr

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024) #changing size from 1024 to 10
    while (l):
       conn.send(l) #made change  here, encode 
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    # conn.send('Thank you for connecting') #commented this line for checking
    conn.close()
