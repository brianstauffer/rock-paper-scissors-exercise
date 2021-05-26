
# game.py

print("Rock, Paper, Scissors, Shoot!")


user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOICE: ", user_choice)

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

print("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")