
st = "\nThis is a new line which is appended to the file."

with open('new-file-1.txt', 'a') as file:
    file.write(st)
    print("Data appended successfully.")

with open('new-file-1.txt', 'r') as file:
    print(file.read())

