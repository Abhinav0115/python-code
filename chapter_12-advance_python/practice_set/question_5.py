'''
Store the multiplication table generate in 'question_3.py' in a file named 'table.txt'. 

'''

n = int(input("Enter a number:"))
table = [i*n for i in range(1,11) ]

# with open("table.txt", "w") as f:
#     for index, item in enumerate(table, start=1):
#         f.write(f"{str(item)}X{index} = {str(item)} \n")
#     print("Table is stored in table.txt file successfully")

with open("table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
print("Table is stored in table.txt file successfully")