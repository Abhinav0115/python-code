'''
A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.

'''

def create_file():
    words = "A file have multile Donkey words. Donkey is a bad word. Donkey is also an animal. "
    with open("some_words.txt", "w") as f:
        f.write(words)


def file_update(word, replace_word):
    with open("some_words.txt", "r") as f:
        content = f.read()

    new_content = content.replace(word, replace_word)

    with open("some_words.txt", "w") as f:    
        f.write(new_content)


create_file()
file_update("Donkey", "######")