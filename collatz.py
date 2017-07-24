def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1

print("Enter a number")
try:
	n = input()
	while True:
		n=int(collatz(n))
		print n
		if n == 1 or n == -1:
			break
except NameError:
	print "Please enter an integer"

