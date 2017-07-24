def func1(l):
	str=""
	for i in range(len(l)-1):
		str += l[i] + ', '
	str = str + 'and ' + l[len(l)-1]
	return str

l=[]
i=0
while True:
	string=raw_input()
	if string == "":
		break
	l.append(string)

print str(func1(l))
