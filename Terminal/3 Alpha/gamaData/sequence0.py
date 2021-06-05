from modules.aestheticFunctions import animations


dialogue = []

with open("sequence0.txt", "r") as rawData:
    for line in rawData:
        dialogue.append(str.strip(line))
rawData.close()
for line in dialogue:
    stringified = str(line)
    stringified.replace("@user", "testName")
    animations.charPrint(stringified)
    input()
