import json
from dialogue import dialogue_dictionary
from functionset import functions


with open("player.json","r") as file:
    dataholder0 = json.load(file)

global username
global progress
global computer

username = dataholder0["username"]
progress = dataholder0["progress"]
computer = "TI-237"

"""
username = "Alex"
progress = "partzero"
computer = "TI-237"
"""

functions.clearTerm()
if __name__ == "__main__":
    dialogue_dictionary[progress].dialogue0(username, computer)
