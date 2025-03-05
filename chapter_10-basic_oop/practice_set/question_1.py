'''
Create a class of the "Programmers" fort storing the information of a programmer working at a Microsoft.

'''


class Programmers:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

    def printDetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Pincode: {self.pincode}, Company: {self.company}")


p1 = Programmers("Henry", 1400000, 145786)
p1.printDetails()
