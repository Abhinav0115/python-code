
def greet(name, message="Good morning!"):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". " + message)


greet('Paul', "Good night!")  # Output: Hello, Paul. Good night!
greet("Rohan")  # Output: Hello, Rohan. Good morning!