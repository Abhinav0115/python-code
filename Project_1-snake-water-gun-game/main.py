'''
Q. Write a python program to implement a snake-water-gun game. 
The game will be played between the computer and the user.

Rules:
1. You have to guess the snake, water, or gun.

Note: You have to use the random module to select the snake, water, or gun randomly.

Example:
Snake vs. Water: Snake wins.
Water vs. Gun: Water wins.
Gun vs. Snake: Gun wins. 

'''
import random

def choiceSelector(c):
    if(c == 1 ):
        return "snake"
    elif ( c == 2 ):
        return "gun"
    elif (c == 3):
        return "water"
    else:
        return "Invalid choice"


def game(user, comp):
    if(user == comp):
        return "Draw"
    else: 
        if(user == 1):
            if(comp == 2):
                return "computer" # user - comp = -1
            elif ( comp == 3):
                return "user" # user - comp = -2
        elif( user == 2):
            if(comp == 1):
                return "user" # user - comp = 1
            elif(comp ==3):
                return "computer" # user - comp = -1
        elif(user == 3):
            if(comp == 1):
                return "computer" # user - comp = 2
            elif ( comp == 2):
                return "user" # user - comp = 1
        else:
            return None

computer  =  random.randint(1, 3)
print(computer)

print("Select your choice: ")
print("1. Snake")
print("2. Gun")
print("3. Water")

user = int(input("Enter your choice: "))

print("User choice: ", choiceSelector(user))
print("Computer choice: ", choiceSelector(computer))

res = game(user, computer)

if(res == None):
    print("Invalid input")
elif(res == "user"):
    print("User win the game")
elif(res == "computer"):
    print("Computer win the game")
elif(res == "Draw"):
    print("Game is Draw")








