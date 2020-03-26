import random
import sys
import time

#FUNCTIONS!!!!
class functions:
    #clear page
    def clearTerm():
        #clear page
        counter = 1
        while counter < 100:
            print("\n")
            counter = counter + 1;

    #Spacer8
    def spacing8():
        #adds 8 clean lines
        counter = 1
        while counter < 9:
            print("\n")
            counter = counter + 1;

    def progressBar():
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
            time.sleep(0.02)
            # Update Progress Bar
            i += 1
            printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
