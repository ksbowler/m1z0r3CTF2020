from Crypto.Util.number import *
import sympy
from secret import p2,q2
import random
import math

f = open("flag.txt")
flag = [s.strip() for s in f.readlines()]
cipher = []
assert len(flag) == 48

#No.1
p1 = getPrime(512)
q1 = getPrime(512)
e1 = 3
n1 = p1*q1
mes1 = ""
for index in range(0,4): mes1 += flag[index]
c1 = pow(bytes_to_long(mes1.encode()),e1,n1)
cipher.append(c1)

#No.2
factor_p2 = sympy.factorint(p2+1)
assert len(bin(p2)) == len(bin(q2))
assert len(factor_p2) == 1
n2 = p2*q2
e2 = 65537
mes2 = ""
for index in range(4,12): mes2 += flag[index]
c2 = pow(bytes_to_long(mes2.encode()),e2,n2)
cipher.append(c2)

#No.3 & No.4
primes = [getPrime(512) for _ in range(3)]
while True:
	num1 = random.randrange(3)
	num2 = random.randrange(3)
	if num1 is not num2: break
n3 = 1
n4 = 1
for i in range(len(primes)):
	if i is not num1: n3 *= primes[i]
	if i is not num2: n4 *= primes[i]
e3 = 65537
e4 = e3
mes3 = ""
mes4 = ""
for index in range(12,18): mes3 += flag[index]
for index in range(18,24): mes4 += flag[index]
c3 = pow(bytes_to_long(mes3.encode()),e3,n3)
c4 = pow(bytes_to_long(mes4.encode()),e4,n4)
cipher.append(c3)
cipher.append(c4)

#No.5
p5 = getPrime(150)
g5 = sympy.primitive_root(p5)
x5 = random.randrange(100000,1000000)
y5 = pow(g5,x5,p5)
r5 = random.randrange(p5-1)
mes5 = ""
for index in range(24,26): mes5 += flag[index]
assert bytes_to_long(mes5.encode()) < p5
c5_1 = pow(g5,r5,p5)
c5_2 = (pow(y5,r5,p5)*bytes_to_long(mes5.encode()))%p5
cipher.append(c5_1)
cipher.append(c5_2)

#No.6
while True:
	p6 = getPrime(256)
	q6 = getPrime(256)
	n6 = p6*q6
	phi6 = (p6-1)*(q6-1)
	if phi6%11 is not 0: break
while True:
	d6 = getPrime(256)
	if math.gcd(d6,phi6) == 1 and math.gcd(d6*11,phi6) == 1:
		break
e6_1 = inverse(d6,phi6)
e6_2 = inverse(d6*11,phi6)
mes6 = ""
for index in range(26,34): mes6 += flag[index]
assert bytes_to_long(mes6.encode()) < n6
c6 = pow(bytes_to_long(mes6.encode()),e6_1,n6)
cipher.append(c6)

#No.7
p7_1 = getPrime(512)
p7_2 = getPrime(512)
p7_3 = getPrime(512)
q7_1 = getPrime(512)
q7_2 = getPrime(512)
q7_3 = getPrime(512)
n7_1 = p7_1*q7_1
n7_2 = p7_2*q7_2
n7_3 = p7_3*q7_3
e7 = 3
mes7 = ""
for i in range(34,48): mes7 += flag[i]
enc7 = bytes_to_long(mes7.encode())
assert enc7 < n7_1
assert enc7 < n7_2
assert enc7 < n7_3
assert pow(enc7,e7) > n7_1
assert pow(enc7,e7) > n7_2
assert pow(enc7,e7) > n7_3
c7_1 = pow(enc7,e7,n7_1)
c7_2 = pow(enc7,e7,n7_2)
c7_3 = pow(enc7,e7,n7_3)
cipher.append(c7_1)
cipher.append(c7_2)
cipher.append(c7_3)

#print public key
print("-----No.1 public key-----")
print("N : ",n1)
print("e : ",e1)
print()

print("-----No.2 public key-----")
print("N : ",n2)
print("e : ",e2)
print()

print("-----No.3 public key-----")
print("N : ",n3)
print("e : ",e3)
print()

print("-----No.4 public key-----")
print("N : ",n4)
print("e : ",e4)
print()

print("-----No.5 public key-----")
print("y : ",y5)
print("g : ",g5)
print("p : ",p5)
print()

print("-----No.6 public key-----")
print("N : ",n6)
print("e1 : ",e6_1)
print("e2 : ",e6_2)
print()

print("-----No.7 public key-----")
print("N1 : ",n7_1)
print("N2 : ",n7_2)
print("N3 : ",n7_3)
print("e : ",e7)
print()

#print ciphertexts
print("-----ciphertexts-----")
ciphertexts = random.sample(cipher,len(cipher))
for enc in ciphertexts: print(enc)
