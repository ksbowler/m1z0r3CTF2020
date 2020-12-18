import itertools


def calcu(score):
	s = 0
	for i in range(1,9):
		#1~8 flame
		if score[i*2] == 10:
			s += 10
			if score[(i+1)*2] == 10: s += 10 + score[(i+2)*2]
			else: s += score[(i+1)*2] + score[(i+1)*2+1]
		elif score[i*2] + score[i*2+1] == 10:
			s += 10 + score[(i+1)*2]
		else: s += score[i*2] + score[i*2+1]

	#9flame
	if score[9*2] == 10:
		s += 10 + score[10*2] + score[10*2+1]
	elif score[9*2] + score[9*2+1] == 10:
		s += 10 + score[10*2]
	else:
		s += score[9*2] + score[9*2+1]

	#10flame
	if score[10*2] == 10:
		s += 10 + score[10*2+1] + score[10*2+2]
	elif score[10*2] + score[10*2+1] == 10:
		s += 10 + score[10*2+2]
	else:
		s += score[10*2] + score[10*2+1]

	return s

def pprint(score):
	for i in range(1,10): print(" "+str(i)+" ",end="")
	print("10 ")
	for i in range(1,10):
		if score[i*2] == 10:
			print(" X ",end="")
		elif score[i*2] + score[i*2+1] == 10:
			print(str(score[i*2])+"/ ",end="")
		else:
			print(str(score[i*2])+str(score[i*2+1])+" ",end="")
	f = ""
	#for i in range(2):
	if score[10*2] == 10:
		f += "X"
		if score[10*2+1] == 10:
			f += "X"
			if score[10*2+2] == 10: f += "X"
			else: f += str(score[10*2+2])
		else:
			if score[10*2+1] + score[10*2+2] == 10: f += str(score[10*2+1])+"/"
			else: f += str(score[10*2+1]) + str(score[10*2+2])
	elif score[10*2] + score[10*2+1] == 10:
		f += str(score[10*2])+"/"
		if score[10*2+2] == 10: f += "X"
		else: f += str(score[10*2+2])
	else:
		f += str(score[10*2])+str(score[10*2+1])
	
		

	print(f)

n,m = map(int,input().split())
#n,m = 3, 10
#n:strike, m:spare
s = [0 for _ in range(23)]
min_score = s
max_score = s
wh = 1
#0:min,1:max
mm = 301
if wh == 0:
	#min
	#X, 1/, 11 のどれか
	t = [i for i in range(1,10)]
	for i in range(0,min(3,n)+1):
		#10flameにあるstrike数 i
		for strike in itertools.combinations(t,n-i):
			s = [0 for _ in range(23)]
			#strikeにはXとなるflameが格納されている
			for k in strike: s[k*2] = 10

			if i <= 1:
				#10Fにstrike一回ならスペアも可能
				s1 = s
				s2 = s
				sp = []
				for j in range(1,11):
					if j in strike: continue
					sp.append(j)
			else:
				sp = []
				for j in range(1,10):
					if j in strike: continue
					sp.append(j)
			#print(i,sp,m)
			#print(s)
			for spare in itertools.combinations(sp,m):
				#print("spare",spare)
				for k in spare:
					s[k*2] = 1
					s[k*2+1] = 9	
					if k == 10:
						if i == 0: s[k*2+2] = 1
						else: s[k*2+2] = 10
						
				if i < 2: mis = [j for j in range(1,11)]
				else: mis = [j for j in range(1,10)]
				for l in strike: mis.remove(l)
				for l in spare: mis.remove(l)
				for l in mis:
					if l == 10:
						if i == 1:
							s[l*2] = 10
							s[l*2+1] = 1
							s[l*2+2] = 1
							continue
					s[l*2] = 1
					s[l*2+1] = 1

				if i > 1:
					for l in range(i): s[10*2+l] = 10
					if i == 2: s[10*2+2] = 1

				temp_score = calcu(s)
				#print(temp_score)
				if temp_score < mm:
					#print(temp_score)
					min_score = s
					#pprint(s)
					#print(s)
					mm = temp_score
				
	print(mm)
	pprint(min_score)
	
else:
	#max
	#X, 9/, 81 のどれか
	mm = -1
	t = [i for i in range(1,10)]
	for i in range(0,min(3,n)+1):
		#10flameにあるstrike数 i
		for strike in itertools.combinations(t,n-i):
			s = [0 for _ in range(23)]
			#strikeにはXとなるflameが格納されている
			for k in strike: s[k*2] = 10

			if i <= 1:
				#10Fにstrike一回ならスペアも可能
				s1 = s
				s2 = s
				sp = []
				for j in range(1,11):
					if j in strike: continue
					sp.append(j)
			else:
				sp = []
				for j in range(1,10):
					if j in strike: continue
					sp.append(j)
			#print(i,sp,m)
			#print(s)
			for spare in itertools.combinations(sp,m):
				#print("spare",spare)
				for k in spare:
					s[k*2] = 9
					s[k*2+1] = 1	
					if k == 10:
						if i == 0: s[k*2+2] = 9
						else: s[k*2+2] = 10
						
				if i < 2: mis = [j for j in range(1,11)]
				else: mis = [j for j in range(1,10)]
				for l in strike: mis.remove(l)
				for l in spare: mis.remove(l)
				for l in mis:
					if l == 10:
						if i == 1:
							s[l*2] = 10
							s[l*2+1] = 8
							s[l*2+2] = 1
							continue
					s[l*2] = 8
					s[l*2+1] = 1

				if i > 1:
					for l in range(i): s[10*2+l] = 10
					if i == 2: s[10*2+2] = 9

				temp_score = calcu(s)
				#print(temp_score)
				if temp_score > mm:
					#print(temp_score)
					max_score = s
					#pprint(s)
					#print(s)
					mm = temp_score
				
	print(mm)
	pprint(max_score)
	
