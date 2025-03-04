''' 
Write a program to generate a multiplication table from 2 to 20 and write it to the file. The table should look like this: 
2 x 1 = 2
2 x 2 = 4
...

write it to the different file. place these files in a folder named "tables". 
'''


import os

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
        
    with open(f"tables/table_of_{n}.txt", "w") as f:
         f.write(table)    

def table(folder_name, init_range, end_range):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    except Exception as e:
        print("Some error occured")
        return
    for i in range(init_range, end_range+1):
        generateTable(i)
                    

# table(folder_name, table_from, table_to)
table("tables", 1, 5)