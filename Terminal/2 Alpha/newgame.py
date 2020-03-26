import json

userdata = {
    "username":"",
    "progress":"partzero"
}

userdata["username"] = str(input("Username: "))
userdata["progress"] = 0

with open("player.json","w") as file:
    json.dump(userdata, file, indent=2)
