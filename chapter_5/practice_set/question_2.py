'''
Q. write a program to get input eight numbers from the user and display all the unique numbers (once).

'''

s = set()
count = 0

while count != 8: 
    num = int(input("Enter the number: "))
    s.add(num)
    count = count+1

print(s)
