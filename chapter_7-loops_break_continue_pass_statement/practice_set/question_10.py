'''
Q. Write a program to print multiplication table of a given number using a for loop in reverse order.

'''



num = int(input("Enter a number: "))

count = 10
for i in range(1, 11):
    print(f"{num}x{count+1-i} = {num * (count-i+1)} ")

