'''
write a program to find the maximum of the number in a list using the reduce function.

'''
from functools import reduce

l = [ 304, 2, 6, 14, 63, 76, 8, 39]


def maximum(x, y):
    if(x>y):
        return x
    return y

result = reduce(lambda x,y: maximum(x, y), l)
result2 = reduce(lambda x,y: x if x>y else y, l)
print(result)
print(result2)