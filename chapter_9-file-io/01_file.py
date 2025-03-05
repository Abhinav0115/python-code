
# File I/O in Python is used to read and write data into a file.
# Python provides basic functions and methods necessary to manipulate files by default.
# You can do most of the file manipulation using a file object.
# The file object provides a set of methods to read and write data into a file.


# ------------- Type of files in Python -------------

# There are two types of files in Python:
# 1. Text files (.txt, .html, .css, .js, .py, etc.)
# 2. Binary files (.jpg, .mp3, .mp4, .pdf, .dat etc.)

# Text files: Text files are normal files that contain the text in the form of characters. These files can be opened and read using any text editor.
# Binary files: Binary files are files that contain the binary data in the form of 0s and 1s. These files can be opened and read using a binary editor.

# Python provides a set of functions and methods to handle both text and binary files.

# ------------- File handling in Python -------------
# File handling is an important part of any application. Python provides a set of functions and methods to handle files.
# The file object is used to read and write data into a file. It provides a set of methods to manipulate files.


file = open("file.txt", "r")
data = file.read()
print("data: ",data)
file.close()

# with statement is used to open a file and close it automatically. It is used to simplify the file handling process.
with open("file.txt", "r") as newFile:
    content = newFile.read()
    print("content: ", content)