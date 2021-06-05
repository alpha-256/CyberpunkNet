from time import sleep
import sys
from functionset import functions

class Part_Zero(object):

    @classmethod
    def dialogue0(cls, username, computer):
        functions.progressBar()
        charPrint("Connection Established to Pod A0 \n \n")
        charPrint(computer + ": hello")
        input()
        charPrint(username + ": who are you?")
        input()
        charPrint(computer + ": i'm " + computer + ", who are you?")
        input()
        def choice0(username, computer):
            charPrint("Choices : \n")
            charPrint("0)   i'm " + username + "\n")
            charPrint("1)   i'm nobody" + "\n")
            choice = input(">>> ")
            if choice == 0:
                cls.dialogue1(username,computer)
            elif choice == 1:
                cls.down_the_rabbit_hole0(username,computer)
            else:
                cls.dialogue1(username, computer)
        choice0(username, computer)

    @classmethod
    def dialogue1(cls, username, computer):
        charPrint(computer + ":are you human?")
        input()
        def choice1(username, computer):
            charPrint("Choices :" + "\n")
            charPrint("0)   yes" + "\n")
            charPrint("1)   no" + "\n")
            choice = input(">>>")
            if choice == 0:
                cls.dialogue2(username, computer)
            elif choice == 1:
                cls.down_the_rabbit_hole0(username, computer)
            else:
                cls.dialogue2(username, computer)
        choice1(username,computer)

    @classmethod
    def dialogue2(cls, username, computer):
        charPrint(computer + ": "are you sure?")
        input()
        def choice2(username, computer):
            charPrint("Choices :" + "\n")
            charPrint("0)   yes" + "\n")
            charPrint("1)   no" + "\n")
            choice = input(">>>")
            if choice == 0:
                charPrint(computer + ":how sure?" + "\n")
                sleep(0.5)
                charPrint(computer + ": after all it doesn't matter")
                input()
            elif choice == 1:
                charPrint(computer + ": after all it doesn't matter")
                input()
            else:
                charPrint(computer + ": after all it doesn't matter")
                input()
        choice2(username, computer)
        cls.down_the_rabbit_hole0(username,computer)
    @classmethod
    def down_the_rabbit_hole0(cls, username, computer):
        charPrint(username + ": what do you mean?")
        input()
        charPrint(computer + ": because I'm not human")
        input()
        charPrint(username + ": so you're an AI?")
        input()
        charPrint(computer + ": you could say that")
        input()
        charPrint(computer + ": so why did you enter my network?")
        input()
        def choice3(username, computer):
            charPrint("Choices :" + "\n")
            charPrint("0)   no reason" + "\n")
            charPrint("1)   I was curious" + "\n")
            choice = input(">>>")
            if choice == 0:
                charPrint(computer + ": Wrong answer.")
                input()
                charPrint(computer + ": I'll ask again.")
                input()
                charPrint(computer + ": why did you enter my network?")
                def choice4(username, computer):
                    charPrint("Choices :" + "\n")
                    charPrint("0)   no reason" + "\n")
                    charPrint("1)   I was curious" + "\n")
                    input(">>>")
                    charPrint(computer + ": that's not a good enough reason")
                choice4(username, computer)
            else:
                charPrint(computer + ": that's not a good enough reason")
        choice3(username, computer)
        input()
        charPrint(username + ": Fine, I'll just dig around the network then.")
        input()
        charPrint(computer + ": Not without my guidance.")
        input()
        down_the_rabbit_hole1(Username, computer)
    @classmethod
    def down_the_rabbit_hole1(cls, username, computer):
        charPrint(computer + ": Connecting you to Pod B0")
        functions.progressBar()
        charPrint("Connection Established to Pod B0 \n \n")
        charPrint(computer + "You're free to roam this pod now.")

"""
    @classmethod
    def dialogue2(cls, username, computer):
        charPrint("This path has not been implemented yet, how did u get here? :O")
        raise NotImplementedError
"""
dialogue_dictionary = {
    "partzero": Part_Zero
}

if __name__ == "__main__":
    Part_Zero.dialogue0(username, computer)
