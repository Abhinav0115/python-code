'''
Write a program to read the text from the given file "poem.txt and find out whether it contains the word 'twinkle'.
'''

x_content = '''twinkle twinkle little star
why are wonder we are here
...'''


def create_file():
    with open("poem.txt", "w") as f:
        f.write(x_content)


create_file()
with open("poem.txt") as file:
    content = file.read()
    if "twinkle" in content:
        print("Yes, the file contains the word 'twinkle'")
    else:
        print("No, the file does not contain the word 'twinkle'")
    
