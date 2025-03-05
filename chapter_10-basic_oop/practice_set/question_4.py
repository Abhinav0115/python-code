'''
Write a class "Calculator" capable of finding square , cube, and square root of a number. Add a static method to greet the user with a message "Hello".

'''

class Calculator: 

    def __init__(self, num):
        self.num = num

    @staticmethod
    def greet():
        print("Helo there")

    def square(self):
        print(f"square of {self.num} is {self.num * self.num}")
    def cube(self):
        print(f"cube of {self.num} is {self.num * self.num * self.num}")
    def squareroot(self):
        print(f"square root of {self.num} is { self.num**1/2}")


num1 = Calculator(4)

num1.greet()
num1.square()
num1.cube()
num1.squareroot()