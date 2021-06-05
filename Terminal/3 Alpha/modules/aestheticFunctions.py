import random
import sys
import time
import os

#FUNCTIONS!!!!
class spacings:
    #clear page
    def clearTerm():
        os.system('cls' if os.name == 'nt' else 'clear')

    #Spacing
    def spacing(lines):
        for iteration in range(0, lines):
            print("")

class animations:

    def charPrint(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.04)

    def progressBar(progressSpeed):
        def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
            formatStr       = "{0:." + str(decimals) + "f}"
            percents        = formatStr.format(100 * (iteration / float(total)))
            filledLength    = int(round(barLength * iteration / float(total)))
            bar             = '█' * filledLength + '-' * (barLength - filledLength)
            sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
            if iteration == total:
                sys.stdout.write('\n')
                sys.stdout.flush()

        # make a list
        items = list(range(0, 100))
        i     = 0
        l     = len(items)

        # Initial call to print 0% progress
        printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
        for item in items:
            # Do stuff...
            time.sleep(progressSpeed)
            # Update Progress Bar
            i += 1
            printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
