print "Enter the string in which you have to count the occurence of each character:"
message=raw_input()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)