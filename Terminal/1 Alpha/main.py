import sys
import math
import time
from functionset import functions
from mainscreen import loadingAnim
from outexport import textLoading

import os
os.environ['LINES'] = "25"
os.environ['COLUMNS'] = "80"

loadingAnim.menuAnimLoad()
input("Press enter to start....")
functions.clearTerm()

if __name__ == "__main__":
    textLoading.dialog_run()
