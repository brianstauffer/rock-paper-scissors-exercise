
# game.py

# get the necessary add ons
import random
import os
import dotenv
dotenv.load_dotenv()

# get the player's name
PLAYER_NAME = os.getenv("PLAYER_NAME")
print (" ")
print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print (" ")
print ("Welcome " + PLAYER_NAME + " to 'Rock, Paper, Scissors, Shoot!'")
print (" ")
print ("------------------------------")

valid_options = ["rock", "paper", "scissors"]

while True:
    while True:
        try:
            user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
            if user_choice in valid_options:
                break
            else:
                print ("OOPS, invalid input. Please try again.")
                print (" ")
                print ("------------------------------")
        except:
           continue
    print (" ")
    print ("------------------------------")
    print (PLAYER_NAME + "'s choice: ", user_choice)
    print (" ")

# computer's choice
    computer_choice = random.choice(valid_options)
    print ("Computer's choice:", computer_choice)
    print ("------------------------------")
    print (" ")
# determine who won!
# adapted from code shared by Jan in Slack
    if user_choice == "rock":
        if computer_choice == "rock":
            print ("It's a tie...want to try again??")
        elif computer_choice == "paper":
            print ("Oh, the computer won...better luck next time")
        elif computer_choice == "scissors":
            print ("YOU WON! Congrats! Try your luck once more?")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print ("YOU WON! Congrats! Try your luck once more?")
        elif computer_choice == "paper":
            print ("It's a tie...want to try again??")
        elif computer_choice == "scissors":
            print ("Oh, the computer won...better luck next time")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print ("Oh, the computer won...better luck next time")
        elif computer_choice == "paper":
            print ("YOU WON! Congrats! Try your luck once more?")
        elif computer_choice == "scissors":
            print ("It's a tie...want to try again??")
    print (" ")
    print ("------------------------------")
# determine whether player wants to play again
# play again code adapted from realpython.com/python-rock-paper-scissors
    play_again = input ("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    print (" ")
    print ("------------------------------")
print (" ")
print ("------------------------------")
print ("This is the end of our game, please play again soon!")
print (" ")
print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print (" ")