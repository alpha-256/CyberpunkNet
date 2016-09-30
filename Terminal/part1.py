import math
import sys
import time
from functionset import functions
from mainscreen import pageone
from newgame import newGame

#story into path 1
class story1:
    def part1():
        def setUsername():
            functions.clearTerm()
            pageone.banner()
            functions.spacing8()
            repr(dict)
            f = open( 'tester.txt', 'w' )
            f.write( 'user1 = ' + repr(userName) + '\n' )
            f.close()
            functions.clearTerm
        def typeAnim(a):
            for char in a:
                time.sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()

        #storyline scentences arranged by alphanumerlogical
        a = "Hello"
        b = "\nWelcome to CyberpunkNet!"

        #start actual story
        userName = input("What is your name? >>>   ")
        setUsername()
        pageone.banner()
        functions.spacing8()
        typeAnim(a)
        typeAnim(b)
        print("\n")
        typeAnim(userName)
