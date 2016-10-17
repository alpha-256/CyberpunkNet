import sys
import math
import time
from functionset import functions
from part1 import story1
from mainscreen import pageone
from newgame import newGame
from loadg import load

#setup function
def setupAll():
    print("     0)   Load Saved File?")
    print("")
    print("     1)   Start New Game?")
    print("")
    print("     99)  Quit Game?")
    chooseStart = int(input("       Select Option by Number pls...>"))
    if chooseStart == 0:
        #loadSaved()
        print("Choose load progress")
        loadSaved()
    elif chooseStart == 1:
        #newGame()
        print("Creating New Game")
        functions.progressBar()
        functions.clearTerm
        newGame.setUsername()
        story1.part1()
        with open('userstat.txt') as f:
            for i, line in enumerate(f, 1):
                if i == num:
                    break
        print(line)
    elif chooseStart == 99:
        exit()
    else:
        exit()


#main menu + animation
pageone.menuAnimLoad()
setupAll()
