# Assignment 1
# PROG 10004
# Rock paper scissors assignment.

from math import *
from random import *


def standings() :
    print(f"The standings are...\nComputer: {computerWins}/{games}.\nPlayer: {playerWins}/{games}")

def computerMath() :
    global computerChoice
    number = (randrange(1,3))
    if number == 1 :
        computerChoice = "R"
    elif number == 2 :
        computerChoice = "P"
    elif number == 3 :
        computerChoice = "S"


def tie() :
    print("You and the computer tied.")
    standings()

def win() :
    playerWins = playerWins + 1
    print("You beat the computer!")
    standings()

def loss() :
    computerWins = computerWins + 1
    print("You lost.")
    standings()


print("------- WELCOME TO ROCK PAPER SCISSORS -------")

games = int(input("How many matches would you like to play?\n> "))
computerWins = 0
playerWins = 0
computerChoice = 0

while playerWins or computerWins < games :
    playerChoice = input("Please select rock (R), paper (P) or scissors (S).")
    computerMath()

    if computerChoice == "R" :
        if playerChoice == "R" :
            tie()
        elif playerChoice == "P" :
            win()
        elif playerChoice == "S" :
            loss()
    elif computerChoice == "P" :
        if playerChoice == "R" :
            tie()
        elif playerChoice == "P" :
            win()
        elif playerChoice == "S" :
            loss()