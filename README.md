# to install, use:

import requests;exec(requests.get("https://raw.githubusercontent.com/MomoCoder123/SimpleSocket/main/install.py").content)

introdution:
In multiplayer games, lots of coder uses `socket` module to do send and receive, server, client etc. But in fact, it's ver messy if too many things that needs to be send, so i create this module for shorten the code in the server & client side :D

# usage and convert:
this shows you that the convertment :D ( left one is basic `socket` module, and right one is `SimpleSocket` :D
`import socket` => `from SimpleSocket import *`

`s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` => `s = createSocket`

`s.bind(("your ip", 8080)); s.listen()` => `listen(s, 8080)`

`conn, addr = s.accept()` => `conn, addr = waitForClient()`

`import threading; threading.Thread(target=handle_client, args=[conn]).start()` => `newThread(handle_client, [conn])`

`socket.gethostbyname(socket.gethostname())` ( not working on pythonista mobile use `s.connect(("google.com", 80)); ip = s.getsockname[0]`) => `getIpAddress()` ( support all devices )

`import pickle; s.send(pickle.dumps([123,12]) + b" " * (64 - len(pickle.dumps([123,12])))` => `send(s, [123,12])`

`s.recv(64)` => `recv(s)`

`s.recv(128)` => `recv(s, maxLen=128)`

`s.send(b"hi" + b" " * (128 - len(b"hi")))` => `send(s, maxLen=128)`
