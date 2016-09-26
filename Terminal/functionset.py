import random
import sys

#FUNCTIONS!!!!
class functions:
    #clear page
    def clearME():
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

    #Confirmersys
    def confirm():
        print("Yes/No?")
        Confirmer = str(input("Y / N ?  >"))
        if Confirmer == "Y" :
            return;
        elif Confirmer == "N" :
            functions.clearME()
            Main.trip()
