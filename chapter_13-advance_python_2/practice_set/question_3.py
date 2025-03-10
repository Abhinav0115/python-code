'''
A list contains the multiplication table of 7. Write a program to convert it into vertical string of the same numbers.


'''

l = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
l = [str(i) for i in l]

print("\n".join(l))