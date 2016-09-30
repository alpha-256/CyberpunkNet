import math
import sys
import time
import os
from functionset import functions
from mainscreen import pageone

class newGame:
    def setUsername():
        functions.clearTerm()
        pageone.banner()
        functions.spacing8()
        userName = input("Username? >>>   ")
        repr(dict)
        f = open( 'tester.txt', 'w' )
        f.write( 'user1 = ' + repr(userName) + '\n' )
        f.close()
        functions.clearTerm
