# There are different methods for file manipulation in Python. They are:

# 1. open() - Open a file in read, write or append mode.
# 2. close() - Close the file. A file should be closed after it has been used.
# 3. write() - Write data into the file. It writes data to a file in a string format.
# 4. read() - Read data from the file. It reads data from the file in a string format.
# 5. readline() - Read a single line from the file. 
# 6. readlines() - Read all the lines from the file and return them as a list. 
# 7. seek() - Change the position of the file pointer.
# 8. tell() - Get the current position of the file pointer.
# 9. truncate() - Remove the contents of the file.
# 10. flush() - Flush the internal buffer. In Python, files are buffered. This means they are read and written in memory before being written to the file.


# ------------ open() ------------
# The open() function is used to open a file. It returns a file object, also called a handle, as it is used to read or modify the file accordingly.
# The open() function takes two parameters; filename, and mode.
# Syntax: 
#   open(file, mode)

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "+" - Open a file for updating (reading and writing)
# "rb" - Read in binary mode
# "wb" - Write in binary mode
# "rt" - Read in text mode (default)
# "wt" - Write in text mode (default)

# Example 1: Open a file
file = open("file.txt", "r")
print(file)


# ------------ close() ------------
# The close() method is used to close a file. A file should be closed after it has been used.
# Syntax: 
#   file.close()

# Example 2: Close a file
file = open("file.txt", "r")
file.close()


# ------------ write() ------------
# The write() method is used to write data into a file. It writes data to a file in a string format.
# Syntax:
#   file.write(data)

# Example 3: Write data into a file
file = open("file.txt", "w")
file.write("Hello, World!")
file.close()


# ------------ read() ------------
# The read() method is used to read data from the file. It reads data from the file in a string format.
# Syntax:
#   file.read()

# Example 4: Read data from a file
file = open("file.txt", "r")
data = file.read()
print(data)
file.close()


# ------------ readline() ------------
# The readline() method is used to read a single line from the file.
# Syntax:
#   file.readline()

# Example 5: Read a single line from a file
file = open("file.txt", "r")
line = file.readline()
print(line)
file.close()


# ------------ readlines() ------------
# The readlines() method is used to read all the lines from the file and return them as a list.
# Syntax:
#   file.readlines()

# Example 6: Read all the lines from a file
file = open("file.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# ------------ seek() ------------
# The seek() method is used to change the position of the file pointer.
# Syntax:
#   file.seek(offset, whence)

# Example 7: Change the position of the file pointer
file = open("file.txt", "r")
file.seek(15)
data = file.read()
print(data)
file.close()


# ------------ tell() ------------
# The tell() method is used to get the current position of the file pointer.
# Syntax:
#   file.tell()

# Example 8: Get the current position of the file pointer
file = open("file.txt", "r")
print(file.tell())
file.close()


# ------------ truncate() ------------
# The truncate() method is used to remove the contents of the file.
# Syntax:
#   file.truncate(size)

# Example 9: Remove the contents of the file
file = open("file.txt", "r+")
file.truncate(5)
data = file.read()
print(data)
file.close()


# ------------ flush() ------------
# The flush() method is used to flush the internal buffer.
# Syntax:
#   file.flush()

# Example 10: Flush the internal buffer
file = open("file.txt")
file.flush()
file.close()
