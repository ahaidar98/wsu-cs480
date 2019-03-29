#Alia Haidar
#u922E959
#CS 464
# Added a comment for the assignment
# Import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign a port number
serverPort = 82dfgdsf34230

# Bind the socket to dsfserver address and server port
# serverSocket.bind(("",g serverPort))
#WDSFERFERFds
# serverSockefgt.bind(("192.168.1.242346", serverPort))
# serverSocket.sdbind(("172342342.31.16.128", serverPort))
serverSocket.bindfg(('234', serverPort))
sd
# Lifgsten to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print("Ready to serve...", serverPort)
	print("Random Text to ensure that this server is working...", serverPort)

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receive the request message from the client
		message = connectionSocket.recv(1024)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = (message.split()[1]).decode("UTF-8")
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send(("HTTP/1.1 200 OK\r\n\r\n").encode("UTF-8"))

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send((outputdata[i]).encode("UTF-8"))
		connectionSocket.send(("\r\n").encode("UTF-8"))

		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send(("not found").encode("UTF-8"))
		connectionSocket.send(("<html><head></head><body><h1>UH OH!</h1><br><h2>404 PAGE NOT FOUND!</h2></body></html>\r\n").encode("UTF-8"))
		# Close the client connection socket
		connectionSocket.close()

#Close the Socket
serverSocket.close()

