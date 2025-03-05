'''
Constructor: A constructor is a special type of method (function) which is used to initialize the instance members of the class.
In python, the __init__() method is called a constructor.
The __init__() method is called when an object is created.
The __init__() method is called automatically when an object is created.
The __init__() method is called a constructor because it initializes the object.
The __init__() method takes self as the first parameter.
The __init__() method takes other parameters that are required to initialize the object.
The __init__() method is called with the class name.

Method start with __ and end with __ is called dunder method.


'''

class employee: 
    salary = 100000     
    language =  "python"

    def __init__(self):
        print("Constructor is called")

    @staticmethod
    def greet(): 
        print("Good Morning")

    def printdetails(self,):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")


harry = employee()
harry.name = "harry"    
harry.language = "java" 
harry.salary = 200000   

harry.printdetails()
harry.greet()



print("\n")


# Example of constructor with parameters
class doctors: 
    salary = 100000     
    speciality =  "cardiologist"

    def __init__(self, name, salary, speciality):
        self.name = name
        self.salary = salary
        self.speciality = speciality
        print("Constructor is called")

    def printdetails(self,):
        print(f"Name: {self.name}, Salary: {self.salary}, Speciality: {self.speciality}")


raman = doctors("Raman", 200000, "neurologist")
raman.printdetails()