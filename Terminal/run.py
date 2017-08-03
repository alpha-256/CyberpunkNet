import sys
import math
import time
from functionset import functions
from storyline import story
from mainscreen import loadingAnim
from banner import logo

import os
os.environ['LINES'] = "25"
os.environ['COLUMNS'] = "80"

loadingAnim.menuAnimLoad()
input("Press enter to start....")
functions.clearTerm()
story.part1()
