'''
List comprehension:
    - A compact way of creating a list
    - It is a syntactic construct that allows you to create a new list by applying an expression to each item in an iterable.
    - It is a concise way of creating a list using a single line of code.

    syntax:
        [expression for item in iterable if condition]
    Example:
        my_list = [x for x in range(10)]
        print(my_list)

'''




l1 = [1,2,4,5,9,7,8]

#basic method:
# squareList = []
# for item in l1:
#     squareList.append(item*item)
# print(squareList)

# Example: Using list comprehension to create a new list
squareList = [i**2 for i in l1]
print(squareList)

