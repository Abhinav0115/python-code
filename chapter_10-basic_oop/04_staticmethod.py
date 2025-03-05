'''
Static Method in Python:
    A static method is a method that doesn't operate on the instance of the class, it doesn't modify the instance of the class.
    A static method is used to perform some operation that is not dependent on the instance of the class.
    A static method can be defined using the @staticmethod decorator.
    A static method doesn't take self as the first argument.

    A static method is a method that is bound to the class and not the object of the class.
    A static method can be called on the class itself without creating an object of the class.
    A static method can access class attributes and can modify class attributes.
    A static method can't access instance attributes and can't modify instance attributes.
    A static method can't access instance methods and can't modify instance methods.
    A static method can't access class methods and can't modify class methods.

'''

class employee: 
    salary = 100000       # Class attributes
    language =  "python"  # Class attributes

    @staticmethod
    def greet():  
        print("Good Morning")

    def printdetails(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

print(employee.salary, employee.language) # Class attributes are shared by all the objects of the class.

harry = employee()
harry.name = "harry"     # Instance attribute
harry.language = "java"  # Instance attribute
harry.salary = 200000    # Instance attribute

harry.printdetails()
harry.greet()
