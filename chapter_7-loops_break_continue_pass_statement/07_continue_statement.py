# continue statement is used to skip the rest of the code inside a loop for the current iteration only.


# Example 1: Using continue statement in a for loop
for i in range(1, 7):
    if i == 3:
        continue
    print(i)
print("End of the loop")
# This code will print numbers from 1 to 6 except 3. When the value of i is 3, the continue statement is executed.


# Example 2: Using continue statement in a while loop
i = 1
while i <= 5:
    if i == 2:
        i += 1 # Incrementing the value of i before the continue statement
        continue
    print(i)
    i += 1
print("End of the loop")
# This code will print numbers from 1 to 5 except 2. When the value of i is 2, the continue statement is executed. The value of i is incremented by 1 before the continue statement is executed to avoid an infinite loop.