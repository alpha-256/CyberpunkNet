import math
import sys
import time
from functionset import functions

#story into path 1
class story1:
    def part1():
        print("Hello")
        print("My name is alan")
        words = "This is just a test :P"
        for char in words:
            sleep(0.5)
            sys.stdout.write(char)
            sys.stdout.flush()
