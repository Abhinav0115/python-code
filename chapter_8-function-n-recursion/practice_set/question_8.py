'''
Q. Write a python function to remove a given word from a list and strip it at the same time.

'''

# Function to remove a word from a list and strip it at the same time
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    

l = ["apple", "banale", "orange", "apple", "banana", "le"]

print(rem(l, "le"))


# function to remove a word from a list 
def remove_word(l, word):
    for item in l:
        l.remove(word)
        return l
    
l = ["apple", "banale", "orange", "apple", "banana", "le"]

print(remove_word(l, "le"))