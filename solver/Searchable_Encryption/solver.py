from Crypto.Util.number import *
#import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import string
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "ys5441.tk", 51696
s, f = sock(HOST, PORT)
print(read_until(f))
flag = "m1z0r3{"
test = []
"""
for ch in string.printable:
	s.send((ch).encode()+b'\n')
	recv_m = read_until(f).split()
	if "Contains" in recv_m:
		test.append(ch)
"""
while True:
	#break
	#for candi in test:
	for candi in string.printable:
		s.send((flag+candi).encode()+b'\n')
		recv_m = read_until(f).split()
		#if "No" in recv_m: continue
		if "Contains" in recv_m:
			flag += candi
			print(flag)
			#print(ord(candi))
			break
		elif not "No" in recv_m:
			print("Finish : ",flag+candi)
			for _ in range(5): print(read_until(f))
			break

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

