'''
Q. Write a program to find the factorial of a number using a while loop

'''

num = int(input("Enter a number: "))

i = 1
fact = 1
while(i<=num):
    fact *= i
    i +=1

print(f"factorial of {num} is {fact}")
