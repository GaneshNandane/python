# simple example snake water gun game 

import random

# Define a function to compare the computer's choice with the user's choice
def check(comp, user):

    # Return 0 if both the computer and user choose the same option
    if comp == user:
        return 0

    # Return -1 if the computer wins against the user
    if comp == 0 and user == 1:
        return -1

    # Return -1 if the computer wins against the user
    if comp == 1 and user == 2:
        return -1

    # Return -1 if the computer wins against the user
    if comp == 2 and user == 0:
        return -1

    # Return 1 if the user wins against the computer
    return 1

# Generate a random number between 0 and 2 for the computer's choice
comp = random.randint(0, 2)

# Ask the user to choose 0 for Snake, 1 for Water, or 2 for Gun
user = int(input("0 for Snake, 1 for Water and 2 for Gun:\n"))

# Compare the computer's choice with the user's choice
score = check(comp, user)

# Print the user's choice
print("You:", user)

# Print the computer's choice
print("Computer:", comp)

# Check whether the computer won
if score == -1:
    print("You Lose")
else:
    # Print that the user won
    print("You Won")
