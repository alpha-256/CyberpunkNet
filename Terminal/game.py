import sys
import math
import time
from functionset import functions
from part1 import story1
from mainscreen import pageone

def setupAll():
    print("0)   Load Saved File?")
    print("")
    print("1)   Start New Game?")
    print("")
    print("99)  Quit Game?")
    chooseStart = int(input(" Select Option by Number pls...>"))
    if chooseStart == 0:
        #loadSaved()
        print("Choose load progress")
    elif chooseStart == 1:
        #newGame()
        print("Load new game function")
    elif chooseStart == 99:
        exit()
    else:
        exit()


#main menu + animation
pageone.menuAnimLoad()

setupAll()