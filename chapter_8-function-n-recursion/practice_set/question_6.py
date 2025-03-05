'''
Q. Write a python program to print the first n line of the following pattern:
***
**
*

'''

def pattern_print(n):
    if(n==0):
        return
    print("*"*n)
    pattern_print(n-1)

n = int(input("Enter a number "))
pattern_print(n)