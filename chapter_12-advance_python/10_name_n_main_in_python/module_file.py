'''
__name__ is a built-in variable in python. It is used to check whether the python script is being run on its own or being imported. If the script is being run on its own, __name__ is set to __main__. If the script is being imported, __name__ is set to the name of the script.

'''


def myFunc():
    print("This is myFunc() function in module.py")

def func2():
    print("This is func2() function in module.py")


if __name__ == "__main__":
    # This block will execute only if this file is executed directly.
    print("The block of code executed directly.")
    myFunc()
else:
    # This block will execute only if this file is imported in another file.
    print("The block of code executed when imported.")

func2()
print(__name__)