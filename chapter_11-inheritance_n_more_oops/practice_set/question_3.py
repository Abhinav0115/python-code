'''
Create a class 'Employee' and add 'salary' and 'increment' properties to it. 

Write a method 'salaryAfterIncrement' with a decorator property with a setter which changes the value of the 'salary'  after increment. 

'''


class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment/100)))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
         self.increment = (salary/self.salary -1) * 100 


a = Employee()
print(a.salaryAfterIncrement)
a.salaryAfterIncrement = 280.8
print(a.increment)