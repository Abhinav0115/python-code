'''
Q. write a program to get input eight numbers from the user and display all the unique numbers (once).

'''

s = set()
count = 0

# Here, I used conditional statement to check if the count is not equal to 8, then take the input from the user and add it to the set.
# We can also solve this question without using the conditional statement as we know that we have to take input from 8 numbers only.

while count != 8: 
    num = int(input("Enter the number: "))
    s.add(num)
    count = count+1

print(s)
