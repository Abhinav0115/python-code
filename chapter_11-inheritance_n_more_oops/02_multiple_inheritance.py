'''
Multiple Inheritance in Python
    - A class can be derived from more than one base classes in Python.
    syntax:
        class Base1:
            pass
        
        class Base2:
            pass
            
        class MultiDerived(Base1, Base2):
            pass

'''


class Employee:
    company = "ITC"
    salary = 10000
    def show(self):
        print(f"The company of the employee is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Your language is {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The company is {self.company} and good with {self.language} language.")



c1 = Employee()
c2 = Programmer()

print("lang ",c2.language)
c2.show()
c2.printLanguages()
c2.showLanguage()

print(c1.company, c2.company)