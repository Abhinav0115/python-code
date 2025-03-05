'''
Q. Write a program to find the sum of first n natural numbers using a while loop.

'''


num = int(input("Enter a number: "))

i = 1
sum = 0

while (i <=num):
    sum += i
    i +=1

print(f"The sum of first {num} natural numbers is {sum}")

