'''
A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.

'''

def create_file():
    words = "A file have multile Donkey words. Donkey is a bad word. Donkey is also an animal. "
    with open("some_words.txt", "w") as f:
        f.write(words)


def file_update(words):
    with open("some_words.txt", "r") as f:
        content = f.read()

    for word in words:
        content = content.replace(word, "#" * len(word))

    with open("some_words.txt", "w") as f:    
        f.write(content)


create_file()
words_list = ["Donkey", "bad", "animal"]
file_update(words_list)