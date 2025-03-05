'''
Create a class with a class attribute a; create an object from it and set a directly using object a=0. Does this change the class attribute?

Ans: No, this does not change the class attribute. The class attribute is shared by all the objects of the class. If we change the class attribute using an object, it will create a new instance of the class attribute for that object. The class attribute will remain the same for all other objects of the class.
'''

class Demo:
    a = 12

    def __init__(self):
        pass

    def printDetails(self):
        print(f"a: {self.a}")

t1 = Demo()
t1.a = 0  #instance attribute
t1.printDetails()


print(Demo.a) #class attribute
