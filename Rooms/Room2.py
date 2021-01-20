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

# commands : 

def Room3Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty):
  print(random.choice(dialog[f"{scene}{roomName2}"]))
  while True:

    if specialRoom == roomName2:
        specialRoom = True

    #Code Here
