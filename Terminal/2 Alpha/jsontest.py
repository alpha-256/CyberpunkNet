import json
import os
from dialogue import zero

with open("player.json","r") as file:
    dataholder0 = json.load(file)

username = dataholder0["username"]
progress = dataholder0["progress"]
global username
global progress
def loadProgress(progress):
