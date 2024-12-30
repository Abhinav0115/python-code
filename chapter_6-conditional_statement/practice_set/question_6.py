'''
Q. Write a program to calculate the grade of a student based on the marks entered by user. The program should work as follows:
90-100: Ex
80-89: A
70-79: B
60-69: C
50-59: D
<50: F

'''


mark = int(input("Enter mark: "))
grade = "F"

if mark>=90 and mark <=100:
    grade = "Ex"
elif mark >=80 and mark <=89:
    grade = "A"
elif mark >=70 and mark <=79:
    grade = "B"
elif mark >=60 and mark <=69:
    grade = "C"
elif mark >=50 and mark <=59:
    grade = "D"
elif mark <50:
    grade = "F"


print("Your grade is:", grade)