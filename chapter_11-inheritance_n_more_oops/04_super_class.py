'''
Super() Method:
    - It is used to call the __init__ method of the super class in the child class.
    - It can also to access the attributes of the super class.

    - Syntax:
        super().__init__()
        super().attribute_name
        super().method_name()
        super().method_name(self)
        super().method_name(arg1, arg2, ...)

'''

class Employee:
    company = "ITC"

    def __init__(self):
        print("Employee created")

class Programmer(Employee):
    salary = 10000
    def __init__(self):
        print("Programmer created")

class Manager(Programmer):
    language = "Python"
    
    def __init__(self):
        super().__init__()
        print("Manager created")


# a = Employee()
# b = Programmer()
c = Manager()


# print(a.company)
# print(b.company, b.salary)
print(c.company, c.salary, c.language)


# ----------------------------------------------------------

class A:
    def some_method(self):
        print("This is method A")

class B:
    def some_method(self):
        print("This is method B")

class C(A, B):
    def some_method(self):
        super().some_method()

c = C()
c.some_method()  #result: This is method A
# In the above example, the method of class A is called because the class A is mentioned first in the inheritance list of class C.