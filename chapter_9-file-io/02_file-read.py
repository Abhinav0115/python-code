

file = open("file.txt", "r")
data = file.read()
print("data: ",data)
file.close()

# The above code is not recommended because if an error occurs after opening the file, the file will not be closed. To avoid this, we can use the with statement.

# with statement is used to open a file and close it automatically. It is used to simplify the file handling process.

with open("file.txt", "r") as newFile:
    content = newFile.read()
    print("content: ", content)