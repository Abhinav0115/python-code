'''
Multilevel Inheritance: 
    - When a class is derived from a class which is also derived from another class.
    - Syntax:
        class BaseClassName:
            pass
            
        class DerivedClassName(BaseClassName):
            pass
            
        class DerivedClassName2(DerivedClassName):
            pass

'''


class Employee:
    company = "ITC"

class Programmer(Employee):
    salary = 10000

class Manager(Programmer):
    language = "Python"

a = Employee()
b = Programmer()
c = Manager()

print(a.company)
print(b.company, b.salary)
print(c.company, c.salary, c.language)