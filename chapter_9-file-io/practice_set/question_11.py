'''
Write a program to rename the file to "rename_by_python.txt".

'''

import os

def create_file(x_content, file_name):
    with open(f"{file_name}.txt", "w") as f:
        f.write(x_content)


def rename_file(filename, new_name):
    os.rename(f"{filename}.txt", f"{new_name}.txt")
    print(f"File renamed to {new_name}.txt")


x = "hello world, X is new social media, that replaced the twitter."
create_file(x, "old")

rename_file("old", "rename_by_python")

