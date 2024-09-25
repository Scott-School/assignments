# Assignment 1
# PROG 10004
# Rock paper scissors assignment.

from math import *
from random import *


def standings() :
    global computerWins
    global games
    global playerWins

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
    global playerWins
    playerWins = playerWins + 1
    print("You beat the computer!")
    standings()

def loss() :
    global computerWins
    computerWins = computerWins + 1
    print("You lost.")
    standings()


print("\n\n------- WELCOME TO ROCK PAPER SCISSORS -------")

games = int(input("How many matches would you like to play?\n> "))
computerWins = 0
playerWins = 0
computerChoice = 0

while playerWins < games and computerWins < games :
    playerChoice = input("\nPlease select rock (R), paper (P) or scissors (S).\n> ")
    playerChoice = playerChoice.upper()
    computerMath()

    if playerChoice == "quit" :
        break
    if computerChoice == "R" :
        if playerChoice == "R" :
            tie()
        elif playerChoice == "P" :
            win()
        elif playerChoice == "S" :
            loss()
    elif computerChoice == "P" :
        if playerChoice == "R" :
            loss()
        elif playerChoice == "P" :
            tie()
        elif playerChoice == "S" :
            win()
    elif computerChoice == "S" :
        if playerChoice == "R" :
            win()
        elif playerChoice == "P" :
            loss()
        elif playerChoice == "S" :
            tie()

if playerWins == games :
    print("You won!")
else :
    print("You lost.")
    
print("Thanks for playing!")