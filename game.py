
# game.py

import random

print("Rock, Paper, Scissors, Shoot!")


user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

print("USER CHOICE:", user_choice)

# validate the input such that only if it is one of hte expected values
# ...will we continue with the rest of the program
# ...otherwise we will stop the program before it tries to do anything else
# ...and we'll ask the user to run the program again

# and
# or

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)

# determine who won!


# adapted from code shared by Reid in Slack

#USER WINNING AND TIE SCENARIOS
if user_choice == computer_choice:
    print("It's a tie, try again!")

elif (user_choice == "scissors") and (computer_choice == "paper"):
    print("Scissors cuts paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
    print("rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print("Paper covers rock, you win!")

#COMPUTER WINNING SCENARIOS
elif (user_choice == "scissors") and (computer_choice == "rock"):
    print("rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
    print("paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
    print("Scissors cuts paper, you lose!")

# configure player name via env variables


print("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")