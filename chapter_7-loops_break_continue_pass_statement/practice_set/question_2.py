'''
Q. Write a program to print multiplication table of a given number using for loop and while loop.

'''


num = int(input("Enter a number: "))


# # m1 - using for loop
for i in range(1,11):
    # print(num,"x", i , " = " , num * i )
    print(f"{num}x{i} = {num*i}")



# m2 - using while loop
count = 1

while count <=10:
    print(f"{num}x{count} = {count*num}")
    count +=1