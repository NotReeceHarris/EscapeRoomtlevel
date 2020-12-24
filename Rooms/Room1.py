import random
import json

jsonFileData = "jsonFiles/data.json"
jsonFileDialog = "jsonFiles/dialog.json"
jsonFileBase = "jsonFiles/BaseData.json"
jsonFileRoom = "jsonFiles/randomRoom.json"

with open(jsonFileDialog, 'r') as a:
    dialog = json.load(a)
with open(jsonFileRoom, 'r') as b:
    roomjson = json.load(b)
with open(jsonFileBase, 'r') as c:
    baseData = json.load(c)
with open(jsonFileData, 'r') as d:
    data = json.load(d)


def Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty):
  while True:

    if specialRoom == roomName1:
        specialRoom = True
    print(random.choice(dialog[f"{scene}{roomName1}"]))
    UserInput = input(str(commandLine.format(roomName1)))  #The input is put in the varaible UserInput

    #Code Here
