import socket                   # Import socket module
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s = socket.socket()             # Create a socket object
# host = socket.gethostname()     # Get local machine name
host = "192.168.43.115"     # Get local machine name
port = 57272       
            # Reserve a port for your service.

s.connect((host, port))
#s.send("Hello server!")

# with open('received_file', 'w') as f:  //commented
#     print ('file opened') //commented
    # while True: // permanenet commented
f=open("Output.txt","w")

while f:    
        print('receiving data...')
        data = s.recv(50000) #problems here check (1) 50000 for full, 50000 for segmented from server 	
        print('data = ', data.decode())
        if not data:
            break
        # write data to a file
        f.write(data.decode())

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
