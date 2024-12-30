'''
Q. Write a program to find the greatest of four numbers entered by the user.

'''

greatest = 0
count = 0
while ( count < 4): 
    num = int(input("Enter number: "))

    if num > greatest: 
        greatest = num
    
    count = count+1


print("greatest number is", greatest)