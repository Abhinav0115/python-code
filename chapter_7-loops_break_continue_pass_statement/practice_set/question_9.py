'''
Q. Write a program to print the following star pattern:

* * * 
*   * 
* * *

for n = 3

'''



n  = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range (1, n+1):
        if(i>1 and i <n):
            if(j==1 or j == n):
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print("*", end="")
    print("")



# m2

for i in range(1, n+1):
    if (i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")
