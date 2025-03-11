'''
Write a program to filter a list of numbers which are divisible by 5.

'''


l = [1, 5, 7, 10, 12, 14, 15, 20, 25, 28, 30, 64, 70]

filteredList = list(filter(lambda x: x%5 ==0, l))
print(filteredList)