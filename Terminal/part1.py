import math
import sys
import time
from functionset import functions
from mainscreen import pageone


#story into path 1
class story1:
    def part1():
        def typeAnim(a):
            for char in a:
                time.sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()

        functions.clearTerm()
        pageone.banner()
        functions.spacing8()
        name  = input("What is your name?  >>>")
        functions.clearTerm

        #storyline scentences arranged by alphanumerlogical
        a = "Hello"
        b = "\nWelcome to CyberpunkNet!"

        #start actual story
        pageone.banner()
        functions.spacing8()
        typeAnim(a)
        typeAnim(b)
        typeAnim(name)
