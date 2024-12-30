
# break statement is used to exit the loop immediately without executing the rest of the code.
# The break statement is used to exit the loop when a certain condition is met.


# Example 1: Using break statement in a for loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("End of the loop")
# This code will print numbers from 1 to 4. When the value of i is 5, the break statement is executed. The loop is terminated immediately without executing the rest of the code.


# Example 2: Using break statement in a while loop
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
print("End of the loop")
# This code will print numbers from 1 to 5. When the value of i is 6, the break statement is executed. The loop is terminated immediately without executing the rest of the code.