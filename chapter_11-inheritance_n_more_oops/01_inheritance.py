'''
Inheritance:
    - Inheritance is a way of creating a new class for using details of an existing class without modifying it.
    - The newly formed class is a derived class (or child class).
    - The existing class is a base class (or parent class).
    - The derived class inherits features from the base class, adding new features to it.
    - This results into re-usability of code.
    - The derived class can have its own features such as methods and properties.
    
'''

'''
Type of Inheritance:
    - Single Inheritance
    - Multiple Inheritance
    - Multilevel Inheritance
    - Hierarchical Inheritance
    - Hybrid Inheritance


Single Inheritance:
    - When a class is derived from only one base class.
    - Syntax:
        class DerivedClassName(BaseClassName):
            pass

Multiple Inheritance:
    - When a class is derived from more than one base class.
    - Syntax:
        class DerivedClassName(BaseClassName1, BaseClassName2, BaseClassName3):
            pass
                       
Multilevel Inheritance:
    - When a class is derived from a class which is also derived from another class.
    - Syntax:
        class BaseClassName:
            pass
            
        class DerivedClassName(BaseClassName):
            pass
            
        class DerivedClassName2(DerivedClassName):
            pass     

Hierarchical Inheritance:
    - When one class is inherited by more than one class.
    - Syntax:
        class BaseClassName:
            pass
            
        class DerivedClassName1(BaseClassName):
            pass
            
        class DerivedClassName2(BaseClassName):
            pass
            
Hybrid Inheritance:
    - Combination of two or more types of inheritance.
    - Syntax:
        class Base1:
            pass
            
        class Base2:
            pass
            
        class DerivedClassName(Base1, Base2):
            pass
'''


class Employee:
    company = "ITC"
    name = "Employee"
    salary = 10000
    def show(self):
        print(f"The name of the employee is  {self.name} and the salary is {self.salary} and the company is {self.company}")



class Programmer(Employee):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The company is {self.company} and salary in the company is {self.salary}.")



c1 = Employee()
c2 = Programmer()


print(c1.company, c2.company)