'''
Q. Write a program to find out whether a student is passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
'''

max_marks  = 300
total_marks = 0

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentage = ((sub1 + sub2 + sub3)*100)/300


print(total_percentage)
if( total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33): 
    print("You passed ", total_percentage)
else:
    print("You Failed ", total_percentage)


# m2
if(total_percentage >= 40):
    if(sub1> 33 and sub2 >= 33 and sub3 >= 33):
        print("You passed")
    else:
        print("You Failed")
else:
    print("You Failed")