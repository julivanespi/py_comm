# Import socket module
import socket

# Create a socket object
s = socket.socket()
print("Created Socket.")

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))
print("Client Connected.")
# close the connection
s.close()
