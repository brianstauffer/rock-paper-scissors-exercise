
# game.py

# get the necessary add ons
import random
import os
import dotenv
dotenv.load_dotenv()

# get the player's name
PLAYER_NAME = os.getenv("PLAYER_NAME")
print ("--------------------")
print("Welcome " + PLAYER_NAME + " to 'Rock, Paper, Scissors, Shoot!'")
print (" ")
print ("--------------------")

valid_options = ["rock", "paper", "scissors"]

while True:
    try:
        user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")
        if user_choice in valid_options:
            break
        else:
            print("OOPS, invalid input. Please try again.")
            print (" ")
            print ("--------------------")
    except:
       continue

#user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

print(PLAYER_NAME + "'s CHOICE:", user_choice)
print ("--------------------")
# validate the input such that only if it is one of hte expected values
# ...will we continue with the rest of the program
# ...otherwise we will stop the program before it tries to do anything else
# ...and we'll ask the user to run the program again

# and
# or

# if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    #print("VALID. KEEP GOING")
# else:
    #print("OOPS, invalid input. Please try again.")
    #exit()

# if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):

# validate player's choice


#if (user_choice not in valid_options):    
    #print("OOPS, invalid input. Please try again!")
    #exit()

# computer's choice
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)
print ("--------------------")

# determine who won!
# adapted from code shared by Jan in Slack
if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE...TRY AGAIN?")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...BETTER LUCK NEXT TIME")
    elif computer_choice == "scissors":
        print("YOU WON! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE...TRY AGAIN?")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...BETTER LUCK NEXT TIME")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("OH, THE COMPUTER WON...BETTER LUCK NEXT TIME")
    elif computer_choice == "paper":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE...TRY AGAIN?")

print ("--------------------")
print("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN!")