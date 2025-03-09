'''
write a list comprehension to print a list which contains the multiplication table of the user entered number.


'''


n = int(input("Enter a number:"))


new_l = [i*n for i in range(1,11) ]
print("Table is:", new_l)