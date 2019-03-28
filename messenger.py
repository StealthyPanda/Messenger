import socket
import _thread


sock = socket.socket()
boo = True


def startnew():
	global sock
	sock.bind((socket.gethostbyname(socket.getfqdn()), 5000))
	print('Convo started. IP is: ' + str(socket.gethostbyname(socket.getfqdn())))
	sock.listen(1)
	con, addr = sock.accept()
	print('\n'+con.recv(1024) + ' joined the convo!')
	sock = con



def join():
	ip = input("\nEnter the convo's IP: ")
	try:
		sock.connect((ip, 5000))
	except:
		print('\nInvalid IP!\n')
		init()
	else:
		sock.send(nick)
		print('\nConnected to someone!')


def getpath():
	path = input('\nEnter the file name or path or drag and drop here: ')
	if path[0] == path[-1] == '\"': path = path[1:-1]
	return path


def deliver():
	global sock
	file = getpath()
	print('\n<!--Tryna send ' + file + ' -->')
	sock.send('<recieve> ' + file)
	acceptance = sock.recv(1024)
	if '<ok>' in acceptance:
		print('\n<!--File accepted. Sending...-->')
		with open(file, 'rb') as f:
			for each in f:
				sock.send(each)
		sock.send('<end>')
		print('<!--File sent successfully!-->')
	else:
		print('<!--File sending failed: reciever rejected request!-->')


def recieve(message):
	global sock
	losbytes = []
	message = message[10:].split('\\')[-1]
	print('\n<!--File incoming: ' + message + ' -->')
	choice = input('\nAccept file? (Y/N): ').lower()
	if choice == 'y':
		sock.send('<ok>')
		print('\n<!--Recieving...-->')
		while True:
			byte = sock.recv(1024)
			if '<end>' in byte:
				break
			else:
				losbytes.append(byte)
		with open(message, 'wb') as file:
			for each in losbytes:
				file.write(each)
		print('\n<!--File recieved successfully!-->\n')
	else:
		sock.send('<no>')





print('\nWelcome to Messenger By StealthyPanda!')
nick = input('\nEnter a nickname: ')
print('\nStart new(n)(0) convo or join(j)(1) a convo:')
def init():
	choice = input('> ').lower()
	if choice in ['n', '0']:
		startnew()
	elif choice in ['j', '1']:
		join()
	else:
		print('\n Invalid choice\n')
		init()
init()

def sender():
	global boo
	while True:
		message = input('\n')
		if message in ['<x>', '<exit>']: 
			sock.close()
			boo = False
			break
		elif '<send>' in message.lower():
			deliver()
		else:
			sock.send(nick + ': ' + message)


def reciever():
	global boo
	while True:
		try:
			recieved = sock.recv(1024)
		except:
			print('\n<!--Convo was terminated by one of the recipients!-->\n')
			break
		if not recieved: 
			sock.close()
			boo = False
			break
		elif '<recieve>' in recieved:
			recieve(recieved)
		else:
			print(recieved + '\n')

_thread.start_new_thread(sender, ())
_thread.start_new_thread(reciever, ())

while boo:
	pass