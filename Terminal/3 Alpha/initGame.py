import json

from aestheticFunctions import spacings
from aestheticFunctions import animations

global userdata
global user
global jsonName
global profilePath
global profileLocation
global username
global progress
global accessLevel

profilePath = "./profiles/"

class prepare:

    def checkUserProgress(user):
        jsonName = user + ".json"
        profileLocation = profilePath + jsonName

        with open(profileLocation) as file:
            userdata = json.load(file)
        file.close()

        username = userdata["Username"]
        progress = userdata["progress"]
        accessLevel = userdata["accessLevel"]

    def loadProgress():
