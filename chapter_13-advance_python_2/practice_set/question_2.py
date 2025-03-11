'''
Write a program to input name, mobile number and marks of a student and format it using the format function like below:
"Hey, my name is [name] and my mobile number is [mobile_number]. I have scored [marks] marks in this exam."`


'''

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
mobile = int(input("Enter your mobile number: "))


print("Hey, my name is {} and my mobile number is {}. I have scored {} in this exam.".format(name, mobile, marks))