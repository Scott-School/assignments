# Assignment 1
# PROG 10004
# Rock paper scissors assignment.
# Scott

from math import *
from random import *

# Displays the computer vs player standings so the player knows how close they are to winning/losing.

computerWins = 0
playerWins = 0
computerChoice = 0
playerChoice = 0
games = 0


def standings() :
    global computerWins
    global games
    global playerWins
    global computerChoice
    global playerChoice

    if computerChoice == "R" :
        computerChoice = "Rock"
    elif computerChoice == "P" :
        computerChoice = "Paper"
    elif computerChoice == "S" :
        computerChoice = "Scissors"

    if playerChoice == "R" :
        playerChoice = "Rock"
    elif playerChoice == "P" :
        playerChoice = "Paper"
    elif playerChoice == "S" :
        playerChoice = "Scissors"
    print(f"Player: {playerChoice} | Computer: {computerChoice}")
    print(f"The standings are...\nComputer: {computerWins}/{games}.\nPlayer: {playerWins}/{games}")


# Makes the computer pick randomly between rock paper and scissors so it can fight the user fairly.
# I found randrange in the random python library!
def randomRPS() :
    global computerChoice

    number = (randrange(1,4))
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
    
def playAgain() :
    global again

    again = input("\nWould you like to play again? (y/N)\n> ")
    again = again.upper()
    again = again[0]

#Initializes Questions:
def initialize() :

    global computerWins
    global playerWins
    global computerChoice
    global playerChoice
    global games

    computerWins = 0
    playerWins = 0
    computerChoice = 0
    playerChoice = 0
    games = 0
    print("\n-------------- WELCOME TO ROCK PAPER SCISSORS --------------")
    print("Instructions:\nYou are playing rock paper and scissors against the worlds strongest super computer.\n If you don't beat it, It will take over the world!")


    # Simple insurance for minimum required number of games.
    while games <= 0 :
        games = int(input("\nHow many matches would you like to play?\n> "))
        if games <=0 :
            print("Please input a valid number of games.")

# Introduces the game to the player.
initialize()

# Main logic loop so that we can tell who wins/loses. 
# Also tells us which score we need to add to.

active = True
while active == True:

    while (playerWins < games) and (computerWins < games) :
        global again
    
        playerChoice = input("\n\nPlease select rock (R), paper (P) or scissors (S).\n> ")

        # Quits application.
        if playerChoice == "quit" :
            playAgain()
            if again == "N" or again == "" :
                break
            else :
                initialize()
                playerChoice = input("\n\nPlease select rock (R), paper (P) or scissors (S).\n> ")


        # Refines player and computer choices so they can be evaluated.
        playerChoice = playerChoice.upper()
        playerChoice = playerChoice[0]
        randomRPS()

        # Logic for computer - rock
        if playerChoice == "R" :

            if computerChoice == "R" :
                tie()
            elif computerChoice == "P" :
                loss()
            elif computerChoice == "S" :
                win()

        # Logic for computer - paper
        elif playerChoice == "P" :

            if computerChoice == "R" :
                win()
            elif computerChoice == "P" :
                tie()
            elif computerChoice == "S" :
                loss()

        # Logic for computer - scissors
        elif playerChoice == "S" :

            if computerChoice == "R" :
                loss()
            elif computerChoice == "P" :
                win()
            elif computerChoice == "S" :
                tie()

        # Ensures only rock paper and scissors are played
        else :
            print("Please input a valid option.")
    

    # Concludes the game with a fun message, and asks to play again.
    if playerWins == games :
        print("\n\n\nYou stopped the computer from taking over!\nCongratulations!   (GOOD ENDING)")

        playAgain()


    elif computerWins == games :
        print("\n\n\nYou let the computer take over... (BAD ENDING)")

        playAgain()


    else :
        break


    if again == "" :
        active = False
    

    elif again[0] == "Y" :
        initialize()


    else :
        active = False

print("Thanks for playing!")