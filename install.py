content = """import sys, pickle, threading, socket as Socket

# -- methods

def getIpAddress():
	try:
		s = Socket.socket()
		s.connect(("google.com", 80))
		return s.getsockname()[0]
	except:
		raise ConnectionError("Please turn on your wifi")

# -- get started : server

def closeServer(socket, stopCode=True):
	socket.close()
	if stopCode:
		sys.exit()
		
def createSocket(family=Socket.AF_INET, type=Socket.SOCK_STREAM):
	return Socket.socket(family, type)
	
def listen(socket, port):
	socket.setsockopt(Socket.SOL_SOCKET, Socket.SO_REUSEADDR, 1)
	socket.bind((getIpAddress(), port))
	socket.listen()
	
def waitForClient(socket):
	conn, addr = socket.accept()
	return conn, addr
	
# -- get started : client

def connect(socket, ip, port):
	socket.connect((ip, port))
	
# -- send & receive

def send(socket, msg, maxLen=64):
	msgType = msg.__class__.__name__
	
	if msgType == "list":
		sendMsg = pickle.dumps(msg)
	else:
		msg = str(msg)
		sendMsg = msg.encode()
	
	sendMsg += b" " * (maxLen - len(sendMsg))
		
	socket.send(sendMsg)
	
def recv(socket, maxLen=64, type="str"):
	if type == "str":
		msg = socket.recv(maxLen)
	else:
		msg = pickle.loads(socket.recv(maxLen))
	return msg

# -- shortens functions

def newThread(target, args=[]):
	threading.Thread(target=target, args=args).start()"""

import os, atexit

path = os.path.join(os.path.expanduser("~"), "Documents/site-packages-3/SimpleSocket")
if os.path.exists(path):
	raise GeneratorExit("You have already installed SimpleSocket")

def createFolder():
	if not os.path.exists(path):
		os.makedirs(path)
		
def createFiles():
	initPath = os.path.join(path, "__init__.py")
	with open(initPath, "x") as f:
		f.write(content)
		
if __name__ == "__main__":
	print("installed zip, ready to extract")
	print("zip is extracted")
	print("downloading module")
	createFolder()
	createFiles()
	print("Downloaded Module : SimpleSocket")
	exit()
