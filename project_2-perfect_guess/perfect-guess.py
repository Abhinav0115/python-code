'''
We are going to write a program that generate a random number and ask the user to guess it.

If the player's guess the higher than the actual number, the program displays "lower number please". Similarly if the user's guess is too low, the program prints "higher number please". When the user guess the correct number, the program display the number of guesses the player used to arrive at the number.

hint: use the random module
'''


from random import randint


def guess_number():
    guesses = 0
    actual_number = randint(1, 666)

    print("Welcome to the guess number game! \nYou have to guess the number that computer generated between 1 and 666.")
    
    player_guessed_number = -1
    while(actual_number != player_guessed_number):
        player_guessed_number = int(input("Please enter the number: "))
        guesses +=1
        
        if player_guessed_number > actual_number:
            print("Please entered lower number ")

        elif player_guessed_number < actual_number:
            print("Please entered higher number ")    

        
    print("You have Guessed the number Correctly!")
    print(f"Total number of attemps takes to guess the number {actual_number} is: {guesses}")


guess_number()