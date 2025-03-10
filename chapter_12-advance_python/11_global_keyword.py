'''
Global Variable:
    - A variable that is defined outside of a function and can be accessed from any function in the program.
    - If a variable is defined inside a function, it is local to that function and cannot be accessed from outside the function.
    - 
    example:
        x = 10
        def my_function():
            print(x)
        my_function() # 10
        print(x) # 10

'''

'''
Global keyword:
    - used to create a global variable inside a function.
    - If a variable is defined inside a function and we want to use it as a global variable, we can use the global keyword.

'''

x = 9999 # global variable

def func():
    x  = 100 # local variable
    print("internal x:", x)

func()
print("global x:", x)

# Using global keyword, we can chnage the value of global variable inside the function.
def new_func():
    global x
    x  = 10 
    print("x after global keyword inside function: ", x)

new_func()
print("x after global keyword outside function:", x) 

# Using global keyword, we make local variable as global variable. Even if the varibale only defined inside the function.
def my_func():
    global y # use global variable
    y = 30
    print("y inside function: ", y)

my_func()
print("y outside function:", y)