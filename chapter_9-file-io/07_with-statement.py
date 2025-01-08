file = open("new-file-1.txt.txt")
print(file.read())
file.close()

# INFO: The above code is not recommended because if an error occurs after opening the file, the file will not be closed. To avoid this, we can use the with statement.

with open("new-file-1.txt", "w") as newFile:
    newFile.write(newData)
