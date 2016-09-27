import math
import sys
import time
from functionset import functions

def typeAnim(a):
    for char in a:
        time.sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()

a = "Hello"
b = "Welcome to CyberpunkNet!"
typeAnim(a)
typeAnim(b)
print("\n")
