
newData = "Something new thing happened today."


# file = open("new-file-1.txt.txt", "w")
# file.write(newData)
# file.close()

# The above code is not recommended because if an error occurs after opening the file, the file will not be closed. To avoid this, we can use the with statement.

with open("new-file-1.txt", "w") as newFile:
    newFile.write(newData)


# with statement is used to open a file and close it automatically. It is used to simplify the file handling process.
with open("new-file-1.txt", "r") as newFile:
    content = newFile.read()
    print("content: ", content)