def pod1(file):
	numbers = []
	f = open(file,"r")
	for l in f:
		if l[0] == l[len(l)-2]:
			numbers.append(l)
	f.close()
	return [len(numbers),int(numbers[0])]
    
print(pod1("liczby.txt"))