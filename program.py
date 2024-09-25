# Assignment 1
# PROG 10004
# Rock paper scissors assignment.

from math import *
from random import *


def computerChoice() :
    print(randrange(1,3))

def tie() :
    print("You and the computer tied.")

def win() :
    playerWins = playerWins + 1
    print("You beat the computer!")

def loss() :
    computerWins = computerWins + 1
    print("You lost.")


print("------- WELCOME TO ROCK PAPER SCISSORS -------")

games = int(input("How many matches would you like to play?\n> "))
computerWins = 0
playerWins = 0

while playerWins or computerWins < games :
    playerChoice = input("Please select rock (R), paper (P) or scissors (S).")
    computerChoice()

    if computerChoice == "R" :
        if playerChoice == "R" :
            tie()
        elif playerChoice == "P" :
            win()
        elif playerChoice == "S" :
            loss()