f = open("part_flag.txt")
a = f.readlines()
flag = ""
cart = ["dog","theory","flower","hated","bone","clumsy","light","dust","good","swamp","lapis","old","smile","pretty","reed","travel","manner","loss","cloth","atten","cry","easy","impossible","lie","well","throat","demon","stench","cheap","lose","perform","fish","fall","chance","appear","head","monkey","hear","ask","negli","eye","body","unknown","edge","poor","gate","back","like","kyoto"]

for c in cart:
	for i in a:
		if c in i:
			print(i)
			flag += i[-2]
			break
print(flag)
