import json
import os
import time

from os import path, listdir
from os.path import isfile, join

from aestheticFunctions import spacings
from aestheticFunctions import animations

from initGame import prepare

global userdata
global jsonName
global user
global profilePath

userdata = str()
jsonName = str()
user = str()
profilePath = "./profiles/"

def newUser():
    #Create base data
    userdata = {
        "username":"",
        "sequence":"0",
        "accessLevel":"10"
    }

    userdata["username"] = str(input("Player Name >>> "))
    userdata["progress"] = 0

    #user
    user = userdata["username"]
    jsonName = user + ".json"
    profileLocation = profilePath + jsonName

    #Check if file Exists
    existCheck = path.exists(profileLocation)

    if existCheck == True:
        print("The username", user, "already exists!")
        print("Go to user loading?")
        confirm = input("[Y/N] >>> ")

        if confirm == "Y":
            animations.progressBar(0.01)
            spacings.clearTerm()
            loadUser()

        elif confirm == "y":
            animations.progressBar(0.01)
            spacings.clearTerm()
            loadUser()

        elif confirm == "N":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.5)

        elif confirm == "n":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.5)
            startMenu()

        else:
            print("Invalid choice!")
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            startMenu()

    else:
        with open(profileLocation, "w") as jsonFile:
            json.dump(userdata, jsonFile, indent=2)
        print("Creating User...")
        animations.progressBar(0.00001)
        print("User Created!")
        time.sleep(0.5)
        spacings.clearTerm()
        loadUser()

#
#        STARTGAME()
#

def initializer(user):
    userdata = None
    jsonName = user + ".json"
    profileLocation = profilePath + jsonName

    with open(profileLocation, "r") as file:
        userdata = json.load(file)
    print(userdata)
    existCheck = path.exists(profileLocation)
    print("Checking system...")
    animations.progressBar(0.00001)

    if existCheck:
        print("Check Complete!")
        print("Errors: 0")
    else:
        print("What the fuck happened?")

    print(user)
    prepare.checkUserProgress(user)

def loadUser():

    print("User Profiles: ")

    fileOnlyFilter = []
    for f in listdir(profilePath):
        if isfile(join(profilePath, f)):
            fileOnlyFilter.append(f)

    print(fileOnlyFilter, "\n")

    user = str(input("Username >>> "))
    jsonName = user + ".json"
    profileLocation = profilePath + jsonName
    existCheck = path.exists(profileLocation)

    if existCheck:
        print("Are you sure you want to load the profile " + user +"?")
        confirm = input("Y/N? >>> ")

        if confirm == "Y":
            spacings.clearTerm()
            print("Loading "+ user +"'s game:")
            animations.progressBar(0.00001)
            with open(profileLocation,"r") as file:
                userdata = json.load(file)
                spacings.clearTerm()
                print("Starting game...")
                animations.progressBar(0.00001)
                spacings.clearTerm()
                user = userdata["username"]
                initializer(user)

        elif confirm == "y":
            spacings.clearTerm()
            print("Loading "+ user +"'s game:")
            animations.progressBar(0.00001)
            with open(profileLocation,"r") as file:
                userdata = json.load(file)
                spacings.clearTerm()
                print("Starting game...")
                animations.progressBar(0.00001)
                spacings.clearTerm()
                user = userdata["username"]
                initializer(user)

        elif confirm == "N":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            spacings.clearTerm()
            startMenu()

        elif confirm == "n":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            spacings.clearTerm()
            startMenu()

        else:
            print("Invalid choice!")
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            spacings.clearTerm()
            startMenu()

    else:
        print("User does not exist!")
        print("Create new user?")
        confirm = input("Y/N? >>> ")

        if confirm == "Y":
            print("\n")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            spacings.clearTerm()
            newUser()

        elif confirm == "y":
            print("\n")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            spacings.clearTerm()
            newUser()

        elif confirm == "N":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            startMenu()

        elif confirm == "n":
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            startMenu()

        else:
            print("Invalid choice!")
            print("Returning to Main Menu...")
            animations.progressBar(0.00001)
            time.sleep(0.2)
            startMenu()

def startMenu():
    spacings.clearTerm()
    print("Welcome to The Array!")
    print("")
    print("0)  Load User")
    print("1)  New User")
    print("99) Exit Game")
    print("")
    selection = input(" >>> ")

    if selection == "0":
        print("\n")
        print("Loading...")
        animations.progressBar(0.00001)
        time.sleep(0.2)
        spacings.clearTerm()
        loadUser()

    elif selection == "1":
        print("\n")
        print("loading...")
        animations.progressBar(0.00001)
        time.sleep(0.2)
        spacings.clearTerm()
        newUser()

    elif selection == "99":
        exit()

    else:
        print("Please type a valid selection!!!")

spacings.clearTerm()
startMenu()
