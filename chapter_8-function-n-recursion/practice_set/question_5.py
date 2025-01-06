'''
Q. Write a recusive function to calculate the sum of first n natural numbers.

'''

def sum_of_n(n):
    if(n==1 ):
        return 1
    
    return n + sum_of_n(n-1)

n = int(input("Enter a number:"))

print(f"sum of {n} natural number is {sum_of_n(n)}")