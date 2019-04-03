from socket import *
# enables to create sockets
serv_addr = "192.168.1.15"
# IP address of the sever
serv_port = 8000
# Port number of the server is given a 16 bit number    
client_sock = socket(AF_INET,SOCK_STREAM)
#The client's socket is created, it will generate a random 16 bit number. First parameter indicates that the underlying network is IPv4, 2nd parameter indicated that it is a TCP socket
client_sock.connect((serv_addr,serv_port))
#The client establishes a TCP connection between the client and server before sending data to the server
msg = input("Enter the text message")
#The client will be asked to input a line until the user ends the line by a carriage return
client_sock.send(msg.encode())
#Sends the encoded string msg through the client's socket, into the TCP connection.
mod_msg = client_sock.recv(2048)
#When characters arrive from the server, they get placed into the string mod_msg.
print("From Server:", mod_msg.decode())
#The message placed in the mod_msg variable is decoded.
client_sock.close()
#Closes the socket, hence closes the TCP connection between the client and the server
