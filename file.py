import socket



sock = socket.socket()
sock.bind()

def sender():
	while True:
		message = raw_input('\n<-- ')
		sock.send(message)
		if message in ['', 'x']: break


def reciever():
	while True:
		recieved = sock.recv(1024)
		print '\n--> ' + recieved + '\n'