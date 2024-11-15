# Use comparison operator to find out wether a given variable a is greater than b or not. (Take a=34 and b=80) 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if a > b: 
    print (a, " is greater than ", b)
elif a == b: 
    print (a, " is equal to ", b)
else: 
    print(a, " is less than ", b)