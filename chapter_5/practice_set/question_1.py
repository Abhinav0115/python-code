'''
Q. Write a program to create a dictionary of hindi words with values as their english translation. Provide the user with an option to look it up!

'''
hindi_dict = {
    "pani": "water",
    "roti": "bread",
    "kutta": "dog",
    "billi": "cat",
    "aam": "mango",
    "kela": "banana",
    "sabzi": "vegetable",
    "phal": "fruit",
    "gadi": "car",
    "makan": "house",
}

entered_word = input("Enter the word you want to know the meaning: ")

# m1 - using get() method to access the dictionary key and the key does not exist, it will return None
# we can use this to check if the key exists in the dictionary or not
result = hindi_dict.get(entered_word)
if(result == None):
    print("No result found for the entered word")
else:
    print("m1 ->", result)


# m2 - if we use [] notation to access the dictionary key and the key does not exist, it will raise a KeyError
# to avoid this, we can use try-except block to handle the KeyError
try:
    other_result = hindi_dict[entered_word]
except(KeyError):
    print("No result found for the entered word")
else:
    print("m2 ->", other_result)