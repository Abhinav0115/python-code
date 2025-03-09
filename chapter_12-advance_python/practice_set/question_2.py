'''
Write a program to print the third, seventh, and fifth element from the list using enumerate() function.


'''

l = [11, 2, 33, 4, 5, 676, 77, 198, 397]

for index, value in enumerate(l, start=1):
    if(index == 3 or index == 5 or index == 7):
        print(f"{index} element is {value}")