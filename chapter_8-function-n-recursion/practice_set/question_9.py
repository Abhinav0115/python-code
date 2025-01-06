'''
Q. Wriet a python function to print multiplication table of a given number.

'''

# Using loop
def multiplication(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication(5)


# Using recursion
def multiplication_table(n, count):
    if(count==11):
        return
    print(f"{n} x {count} = {n*count}")
    multiplication_table(n, count+1)


multiplication_table(5, 1)