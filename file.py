import socket
import thread
import os


sock = socket.socket()


def startnew():
	sock = socket.socket()
	sock.bind((socket.gethostname(), 5000))
	print 'Convo started. IP is: ' + str(socket.gethostname())
	sock.listen(1)
	con, addr = sock.accept()
	print str(addr) + ' joined the convo!'
	sock = con



def join():
	ip = raw_input("Enter the convo's IP: ")
	sock.connect((ip, 5000))





print '\nWelcome to Messenger By StealthyPanda!'
print 'Start new(n)(0) convo or join(j)(1) a convo:'
def init():
	choice = raw_input('> ').lower()
	if choice in ['n', '0']:
		startnew()
	elif choice in ['j', '1']:
		join()
	else:
		print '\n Invalid choice\n'
		init()
init()

def sender(sock):
	while True:
		message = raw_input('\n<-- ')
		if message in ['', 'x']: break
		sock.send(message)


def reciever(sock):
	while True:
		recieved = sock.recv(1024)
		if not r: break
		print '\n--> ' + recieved + '\n'

thread.start_new_thread(sender, (sock, ))
thread.start_new_thread(reciever, (sock, ))

while True:
	pass