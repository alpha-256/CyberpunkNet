from time import sleep
inventoryItems = []
playername = []
progressState = 0
bedroomOptions = ["Sleep", "Nap", "Lay Down", "Sit", "go to"]
bedroomDoors = ["Bathroom", "Living room / Kitchen"]

def part0():
    print("It's 5:30 in the morning")
    sleep(0.5)
    print("You woke up in your appartment on your couch nauseating and tremblng from cold sweat")
    sleep(0.5)
    print("What do you do?")
    sleep(0.5)
    for item in bedroomOptions:
        print("\n")
        print(item)
        sleep(0.5)
    q0 = input("yes or no?")
    if q0 == "yes":
        playername.append(input("What's your name?"))
    else:
        print("Where to go?")
        print("")
        playername.append(input("What's your name?"))
if progressState == 0:
    part0()
