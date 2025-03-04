'''
The game() function in the program lets a user play a game and return the score as an integer. You need to read the "Hi-score.txt", which is eithe blank or contains the previous hi-score. You need to update the hi-score if the user beats the hi-score. You need to write the new hi-score back to the file.   
'''


def game():
    new_value = int(input("Enter new score:"))
    with open("Hi-score.txt") as file:
        content = file.read()
        if (int(content) < new_value or content == ""):
            print("We have new high score")
            with open("Hi-score.txt", "w") as new_file:
                new_file.write(str(new_value))
        else:
            print("High score is ", content)


game()