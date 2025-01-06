'''
Q. Write a program to find the greatest of the three numbers using a function.

'''


def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    

n1 =  int(input("Enter 1st Number: "))
n2 =  int(input("Enter 2nd Number: "))
n3 =  int(input("Enter 3rd Number: "))


print(f"{greatest(n1,n2, n3)} is the greatest number")