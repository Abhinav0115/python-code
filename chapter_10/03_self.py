'''
self in python:
    self is a reference to the current instance of the class, and is used to access variables that belong to the class.
    It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
    self is not a keyword in python, it is just a convention.
    self is a reference to the instance of the class.
    self is used to access the attributes of the class.
'''

'''
when we call a method of a class, it automatically passes the instance as the first argument to the method.    
example:
    harry.printdetails() is equivalent to employee.printdetails(harry)
    In the above example, harry is passed as the first argument to the printdetails() method.
    Therefore, the first parameter of the printdetails() method is the instance harry itself.
    This parameter is named self by convention.
    Therefore, the first parameter of the printdetails() method is self.

'''



class employee: 
    salary = 100000       # Class attributes
    language =  "python"  # Class attributes

    # def greet():  #this will give error because greet() method takes 0 positional arguments but 1 was given
    def greet(self):  
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

rohan = employee()
rohan.name = "rohan"    # Instance attribute
rohan.language = "c++"  # Instance attribute

# rohan.printdetails()
employee.printdetails(rohan)
