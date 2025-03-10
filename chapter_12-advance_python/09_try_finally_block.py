'''
Try Finally Block
    - The finally block is used to execute a block of code regardless of the result of the try block.
    - Finally block will execute even after the return statement.


'''

try:
    a = int(input("Enter first number: "))
    print(a)
except Exception as e:
    print("Exception occurred: ", e)

finally: 
    print("This block will always execute")


print("------------------------------")

def main():
    try:
        print("Hello")
        return
    except Exception as e:
        print("Exception occurred: ", e)
        return
    finally:
        print("This block will always execute even after return statement")

main()