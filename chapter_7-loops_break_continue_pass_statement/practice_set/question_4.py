'''
Q. Write a program to find whether a given number is prime or not.

'''


num = int(input("Enter a number: "))

i = 2
while ( i <= num-1):
    if(num % i == 0 ):
        print(f"{num} not a prime number")
        break
    i +=1
else: 
    print(f"{num} is a prime number {i}")