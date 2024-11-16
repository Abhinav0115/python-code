#  wriet a python program to fill in a letter template given below with name and date.
# letter = '''Dear <|Name|>,
# Greetings from ABC coding house. I am happy to tell you about your selection
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Bill
# Date: <|Date|>'''


name = input("Enter your name: ")
date = input("Enter date: ")

letter = '''Dear <|Name|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|Date|>'''

# method 1: using f-string
newLetter = f'''Dear {name},
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: {date}'''

print(newLetter)

# method 2: using string.replace() method
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
