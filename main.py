# --------------------------------------- Imports

import random
import time
from inventorySystem import SeeI, AddI, DropI
import json

# --------------------------------------- Variables

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

mainCharacter = random.choice(baseData["mainCharacterNames"])
sideCharacter = random.choice(baseData["sideCharacterNames"])
antagonistCharacter = random.choice(baseData["antagonistNames"])
scene = random.choice(baseData["Scene"])
roomName1 = random.choice(roomjson[f'{scene}1'])
roomName2 = random.choice(roomjson[f'{scene}2'])
roomName3 = random.choice(roomjson[f'{scene}3'])
roomName4 = random.choice(roomjson[f'{scene}4'])
roomName5 = random.choice(roomjson[f'{scene}5'])
specialRoom = random.choice([roomName1, roomName2, roomName3, roomName4, roomName5])
inventorySpace = data["inventorySpace"]
specialItem = random.choice(baseData[f"{scene}SpecialItem"])

# --------------------------------------- Start Function

def startGame():
  if data["Debug"]:
    print(dialog["debug"].format(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, inventorySpace, specialItem, specialRoom))
  print(dialog["start"])
  input('\nPress Enter to start...')
  global Start
  Start = time.time()
  print('\n')
  


# --------------------------------------- Corridor Function

def Corridor():
  print()

#---RoomA
def roomA():
  print('')





#--------------------------------------- Start of Script

startGame()