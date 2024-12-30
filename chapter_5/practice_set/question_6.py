'''
Create and empty dictionary and allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

'''

fav_lang = {}

count = 0
while count !=4:
    name= input("Enter your name: ")
    lang = input("Enter your fav language: ")

    fav_lang.update({name: lang})
    count = count +1


print(fav_lang)