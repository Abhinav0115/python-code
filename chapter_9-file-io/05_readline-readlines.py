
# readline() reads one line at a time
file = open('file.txt', 'r')
print("line 1 ", file.readline())
print("line 2 ", file.readline())
print("line 3 ", file.readline())
print("line 4 ", file.readline())

file.flush()
file.close()


# readlines() reads all the lines at once
file = open('file.txt', 'r')
lines = file.readlines()
types = [type(lines)]
print(lines)
print(types)

file.flush()
file.close()