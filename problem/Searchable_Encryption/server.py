import socketserver
import signal
import random
import time
import hashlib
from FLAG import flag

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		req = self.request
		#signal.alarm(300)
		gr = "Welcome to Searchable Encryption.\n"
		req.sendall(bytes(gr,'utf-8'))
		f = open("keywords.txt")
		keywords = [s.strip() for s in f.readlines()]
		while True:
			key = req.recv(4096).strip()
			if key == flag:
				fin = "Congratulation! You find a flag!\n"
				req.sendall(bytes(fin,'utf-8'))
				req.sendall(flag + b'\n')
				break

			if str(hashlib.sha256(key).hexdigest()) in keywords:
				s = "Contains\n"
			else:
				s = "No\n"
			req.sendall(bytes(s,'utf-8'))


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass


socketserver.TCPServer.allow_reuse_address = True
server = ReusableTCPServer(("0.0.0.0", 51696), incoming)
server.serve_forever()

