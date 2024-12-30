# Write a python program to print the contents of a directory using the OS module.

import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        # Print each item in the directory
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to list
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
