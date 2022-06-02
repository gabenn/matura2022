def pod1(file):
	numbers = []
	f = open(file,"r")
	for l in f:
		if l[0] == l[len(l)-2]:
			numbers.append(l)
	f.close()
	return [len(numbers),int(numbers[0])]
	
print(pod1("./liczby.txt"))
def pod2(file):
	f = open(file,"r")
	a1 = [0,0]
	a2 = [0,0]
	for l in f:
		number = int(l)
		ilCzynnikow = 0
		i=1
		while i < int(number**1/2+1):
			if number % i == 0:
				ilCzynnikow +=1
				number/=i
				i=1
			i+=1
						
		if a1[1] < ilCzynnikow:
			a1[0] = int(l)
			a1[1] = ilCzynnikow
		
		number=int(l)
		ilCzynnikow2 = 0
		for j in range(2,int(number**1/2+1)):
			if number % j == 0:
				ilCzynnikow2 +=1
				number/=j
						
		if a2[1] < ilCzynnikow2:
			a2[0] = int(l)
			a2[1] = ilCzynnikow2
		
	return [a1,a2]

print(pod2("./przyklad.txt"))		

def pod3(file):
	liczby = []
	
	for l in open(file,"r"):
			n1 = int(l)
			for l2 in open(file,"r"):
					n2 = int(l2)
					if n1!=n2 and n2%n1==0:
							for l3 in open(file,"r"):
									n3 = int(l3)
									if n3!=n1 and n3!=n2 and n3%n2==0:
											liczby.append([n1,n2,n3])
	output = open("trojki.txt","a")
	for i in range(len(liczby)):
		output.write(f"{liczby[i][0]} {liczby[i][1]} {liczby[i][2]}\n")
	return [len(liczby),liczby]
		
print(pod3('./przyklad.txt'))