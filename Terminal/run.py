import sys
import math
import time
from functionset import functions
from storyline import story
from mainscreen import loadingAnim
from banner import logo

loadingAnim.menuAnimLoad()
input("Press enter to start....")
functions.clearTerm()
story.part1()
