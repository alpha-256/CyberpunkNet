import math
import sys
import time
from functionset import functions
from time import sleep as wait

#story into path 1
class story:
    def part1():
        with open("story.txt","r") as f:
                for line in f:
                    if '\n' == line[-1]:
                        line = line[:-1]
                        input()
                        print(line)
