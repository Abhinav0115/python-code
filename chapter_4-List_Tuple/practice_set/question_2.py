# write a program to accepts marks of the 6 students in a list and then finally display the marks in a sorted manner.

marks = []

for i in range(6):
    mark = int(input("Enter mark: "))
    marks.append(mark)

marks.sort()

print(marks)