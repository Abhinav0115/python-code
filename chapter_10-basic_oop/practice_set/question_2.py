'''
Write a class "Calculator" capable of finding square , cube, and square root of a number

'''
import math

class Calculator: 

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"square of {self.num} is {self.num * self.num}")
    def cube(self):
        print(f"cube of {self.num} is {self.num * self.num * self.num}")
    def sqrt(self):
        print(f"square root of {self.num} is { math.sqrt( self.num)}")
    def squareroot(self):
        print(f"square root of {self.num} is { self.num**1/2}")


num1 = Calculator(4)

num1.square()
num1.cube()
num1.sqrt()
num1.squareroot()