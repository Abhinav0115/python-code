'''
enumerate():
    - enumerate() is a built-in function that allows you to loop over an iterable and have an automatic counter.
    - It returns an enumerate object, which is an iterator that produces pairs of index and value.
    - The enumerate object can be converted to a list or tuple using the list() or tuple() functions.
    - The enumerate() function takes two arguments:
        - iterable: the iterable to loop over
        - start: the starting index (default is 0)
    
    - The enumerate() function is useful when you need to keep track of the index of the current item in a loop.
    - The enumerate() function is often used in conjunction with the for loop.

    syntax:
        enumerate(iterable, start=0)
    Example:
        my_list = ['apple', 'banana', 'cherry']
        for index, value in enumerate(my_list):
            print(index, value)
    Output:
        0 apple
        1 banana
        2 cherry

'''

#Example: Using default method using loop
l = [3,44,555,8888,99999]

index = 0
for item in l:
    print(f"item at index {index} is {item}")
    index += 1

print("-------------------------------------")
# Example: Using enumerate() method with a list
for index, item in enumerate(l, start=11): #by default start is 0
# for index, item in enumerate(l):
    print(f"(Using enumerate) The item at index {index} is {item}")
