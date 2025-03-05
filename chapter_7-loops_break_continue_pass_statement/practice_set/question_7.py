'''
Q. Write a program to print the following star pattern:

  *  
 ***
*****

for n = 3

'''


n  = int(input("Enter a number: "))


# m1 - using loops
for i in range(1, n+1):
    for j in range (1, n+1-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print("")


# m2 - using string multiplication       
for i in range(1, n+1):
        print(" " * (n-i), end="")
        print("*" * (2*i-1))