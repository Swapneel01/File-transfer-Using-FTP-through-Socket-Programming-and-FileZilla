from socket import *
serv_addr = "192.168.1.15"
serv_port = 8000
serv_sock = socket(AF_INET,SOCK_STREAM)
serv_sock.bind((serv_addr,serv_port))
serv_sock.listen(1)
print("The server is ready to receive")
while 1:
     conn_sock,client_addr = serv_sock.accept()
     print("Got connection from", client_addr)
     # print("message",conn_sock)
     msg = conn_sock.recv(2048)
     # print("message",msg)
     print(msg.decode())
     mod_msg = msg.upper()
     conn_sock.send(mod_msg)
     conn_sock.close()
