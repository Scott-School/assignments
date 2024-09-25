# Assignment 1
# PROG 10004
# Rock paper scissors assignment.
# This is not complex and doesn't require multiple files.

from math import *
from random import *

# Displays the computer vs player standings so the player knows how close they are to winning/losing.
def standings() :
    global computerWins
    global games
    global playerWins
    global computerChoice
    global playerChoice

    print(f"Computer: {computerChoice} vs Player: {playerChoice}")
    print(f"The standings are...\nComputer: {computerWins}/{games}.\nPlayer: {playerWins}/{games}")


# Makes the computer pick randomly between rock paper and scissors so it can fight the user fairly.
def randomRPS() :
    global computerChoice
    number = (randrange(1,3))
    if number == 1 :
        computerChoice = "R"
    elif number == 2 :
        computerChoice = "P"
    elif number == 3 :
        computerChoice = "S"

# It runs this and doesn't update any info if the player and computer tie.
def tie() :
    print("You and the computer tied.")
    standings()

# Is run when the player wins.
def win() :
    global playerWins
    playerWins = playerWins + 1
    print("You beat the computer!")
    standings()
    
# Is run when the player loses.
def loss() :
    global computerWins
    computerWins = computerWins + 1
    print("You lost.")
    standings()
    


# Introduces the game to the player.

print("\n-------------- WELCOME TO ROCK PAPER SCISSORS --------------")
print("Instructions:\nYou are playing rock paper and scissors against the worlds strongest super computer.\n If you don't beat it, It will take over the world!")
games = int(input("\nHow many matches would you like to play?\n> "))
computerWins = 0
playerWins = 0
computerChoice = 0
playerChoice = 0

# Main logic loop so that we can tell who wins/loses. 
# Also tells us which score we need to add to.

while playerWins < games and computerWins < games :
    playerChoice = input("\n\nPlease select rock (R), paper (P) or scissors (S).\n> ")

    # Refines player and computer choices so they can be evaluated.
    playerChoice = playerChoice.upper()
    randomRPS()

    # Quits application.
    if playerChoice == "quit" :
        break

    # Logic for computer - rock
    if computerChoice == "R" :

        if playerChoice == "R" :
            tie()
        elif playerChoice == "P" :
            win()
        elif playerChoice == "S" :
            loss()

    # Logic for computer - paper
    elif computerChoice == "P" :

        if playerChoice == "R" :
            loss()
        elif playerChoice == "P" :
            tie()
        elif playerChoice == "S" :
            win()

    # Logic for computer - scissors
    elif computerChoice == "S" :

        if playerChoice == "R" :
            win()
        elif playerChoice == "P" :
            loss()
        elif playerChoice == "S" :
            tie()


# Concludes the game with a fun message!

if playerWins == games :
    print("\n\n\nYou stopped the computer from taking over!\nCongratulations! (GOOD ENDING)")
else :
    print("\n\n\nYou let the computer take over... (BAD ENDING)")

print("Thanks for playing!")