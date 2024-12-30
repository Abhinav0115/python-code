'''
Q. Write a program to find out whether a given post is talking about "Harry" or not.

'''

post = input("Enter post message: ")

if("harry" in post.lower()  ):
    print("Yes, the post is talking about Harry")
else:
    print("No, the post is not talking about Harry")