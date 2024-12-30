'''
Create and empty dictionary and allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

'''

fav_lang = {}


# Here, I used conditional statement to check if the count is not equal to 4, then take the input from the user and add it to the dictionary.
# We can also solve this question without using the conditional statement as we know that we have to take input from 4 friends only.
count = 0
while count !=4:
    name= input("Enter your name: ")
    lang = input("Enter your fav language: ")

    fav_lang.update({name: lang})
    count = count +1


print(fav_lang)