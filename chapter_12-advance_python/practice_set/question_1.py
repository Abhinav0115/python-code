'''
Write a program to open three files 1.txt, 2.txt and 3.txt, if any of these files not present, a message without existing the program must be printed prompting the same.   

'''


def create_file(file_name, text):
    with open(f"{str(file_name)}.txt", "w") as f:
        f.write(text)

create_file(1, "1st file data")
# create_file(2, "2nd file data")
create_file(3, "3rd file data")

try:
    with open("1.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print("File not found", e)


try:
    with open("2.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnf:
    print(fnf.filename, "file not found" )


try:
    with open("3.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnf:
    print(fnf.filename, "file not found" )

except Exception as e:
    print("File not found", e)



print("Program ended successfully!")
