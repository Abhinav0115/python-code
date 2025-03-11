'''
map() 
    - map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    syntax:
        map(function, iterable)
            - function: The function to execute for each item
            - iterable: The iterable to be processed
'''
'''
filter()
    - The filter() method constructs an iterator from elements of an iterable for which a function returns true.
    - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    syntax:
        filter(function, iterable)
            - function: The function to execute for each item
            - iterable: The iterable to be processed

'''
'''
reduce()
    - The reduce() function is defined in the functools module.
    - The reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
    - The reduce() function reduces a list to a single value by combining elements via a supplied function.
    syntax:
        reduce(function, iterable)
            - function: The function to execute for each item
            - iterable: The iterable to be processed
    example:
        l = [1, 2, 3, 4]
        def multiply(x, y):
            return x*y

        res = reduce(multiply, l)
        steps:
            - 1*2 = 2
            - 2*3 = 6
            - 6*4 = 24
        print(res)  # Output: 24

'''


# Example 1: map() function

l = [1, 2, 3, 4, 5]
square = lambda x: x*x

sqList = map(square, l)
print("Map:",sqList)  # Output: <map object at <address> >
res = list(sqList)
print("Map:",res)  # Output: [1, 4, 9, 16, 25]


#Example 2: filter() function
l = [1, 2, 3, 4, 5]

filteredList = filter(lambda x: x%2==0, l)
print("Filter:",list(filteredList))


# Example 3: reduce() function
 
from functools import reduce

l = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, l)
print("Reduce:", sum)  # Output: 15
multiply = reduce(lambda x, y: x*y, l)
print("Reduce:", multiply)  # Output: 120
