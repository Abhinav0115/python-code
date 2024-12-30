'''
Q. A spam comment is defined as a text containing the following keywords: "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

'''

spam = ["make a lot of money", "buy now", "subscribe this", "click this"]
comment = input("Enter your comment: ")
is_spam = False


if ("make a lot of money" in comment) or ("buy now" in comment) or ("subscribe this" in comment) or ("click this" in comment):
    is_spam = True


if is_spam:
    print("This comment is a spam")
else: 
    print("This comment is not a spam")


# for i in spam:
#     if i in comment: 
#         print("This comment is a spam")
#     else: 
#         print("This comment is not a spam")
