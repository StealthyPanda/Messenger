import socket
import thread


sock = socket.socket()
boo = True


def startnew():
	global sock
	sock.bind((socket.gethostname(), 5000))
	print 'Convo started. IP is: ' + str(socket.gethostbyname(socket.getfqdn()))
	sock.listen(1)
	con, addr = sock.accept()
	print '\n'+con.recv(1024) + ' joined the convo!'
	sock = con



def join():
	ip = raw_input("Enter the convo's IP: ")
	try:
		sock.connect((ip, 5000))
	except:
		print '\nInvalid IP!\n'
		init()
	else:
		sock.send(nick)
		print '\nConnected to someone!'





print '\nWelcome to Messenger By StealthyPanda!'
nick = raw_input('\nEnter a nickname: ')
print '\nStart new(n)(0) convo or join(j)(1) a convo:'
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

def sender():
	global boo
	while True:
		message = raw_input('\n')
		if message in ['', 'x']: 
			sock.close()
			boo = False
			break
		sock.send(nick + ': ' + message)


def reciever():
	global boo
	while True:
		try:
			recieved = sock.recv(1024)
		except:
			print '\n<!--Convo was terminated by one of the recipients!-->\n'
			break
		if not recieved: 
			sock.close()
			boo = False
			break
		print recieved + '\n'

thread.start_new_thread(sender, ())
thread.start_new_thread(reciever, ())

while boo:
	pass