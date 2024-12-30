'''

problem 6: Create and empty dictionary and allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

Q. If the language of the two friend are same; what will happen to the program in problem 6?

'''

# Solution: This will create a dictionary with the name as key and the language as value. If the language is same, the last language entered by the user will be the value of the that key.

fav_lang = {}

count = 0
while count !=4:
    name= input("Enter your name: ")
    lang = input("Enter your fav language: ")

    fav_lang.update({name: lang})
    count = count +1


print(fav_lang)