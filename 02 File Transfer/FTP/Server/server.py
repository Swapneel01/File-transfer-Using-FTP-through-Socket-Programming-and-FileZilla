##########################################

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()

########### USERS ####################
#first parameter is the username, second one is the password and the third one is the directory to which that particular user has access to

authorizer.add_user("Swapneel", "Swapneel", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Swarna", "Swarna", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Sumukh", "Sumukh", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Suhaas", "Suhaas", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Param", "Param", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Akash", "Akash", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("Sumanth", "Sumanth", "D:\Demo", perm="elradfmwMT")

######################################

authorizer.add_anonymous("D:\Demo") #path of the directory you want to the clients to access
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("192.168.43.115", 21), handler) #the IP address of your system, the one which is the server
server.serve_forever()
