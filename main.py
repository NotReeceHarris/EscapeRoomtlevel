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
commandLine = '\nRoom: {}  |  Commands: Help, Inventory\n >#> '

# --------------------------------------- Start Function

def startGame():
  if data["Debug"]:
    print(dialog["debug"].format(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, inventorySpace, specialItem, specialRoom))
  print(dialog["start"])
  input('\nPress Enter to start...')
  global Start
  Start = time.time()
  print(dialog["dialog1.0"].format(antagonistCharacter))
  input()
  print(dialog["dialog1.1"])
  input()
  print(dialog["dialog1.2"])
  input()
  print(dialog["dialog1.3"].format(mainCharacter))
  input()
  print(dialog["dialog1.4"])
  input()
  print(dialog["dialog1.5"].format(mainCharacter, mainCharacter))
  input()
  print(dialog["dialog1.6"].format(sideCharacter))
  input()
  print(dialog["dialog1.7"].format(mainCharacter))
  input()
  print(dialog["dialog1.8"].format(sideCharacter, scene))
  input()
  print(dialog["dialog1.9"].format(mainCharacter, scene))
  input()
  print(dialog["dialog1.10"].format(sideCharacter))
  input()
  print(dialog["dialog1.11"].format(mainCharacter))
  input()
  print(dialog["dialog1.12"].format(sideCharacter))
  input()
  print(dialog["dialog1.13"].format(mainCharacter))
  input()
  print(dialog["dialog1.14"])
  input()
  print(dialog["dialog1.15"].format(sideCharacter))
  input()
  userInput = input(str(commandLine.format('Outer Rooms')))
  


# --------------------------------------- Corridor Function

def Corridor():
  print()

#---RoomA
def roomA():
  print(random.choice(dialog[f"{scene}{roomName1}"]))

#---RoomB
def roomB():
  print(random.choice(dialog[f"{scene}{roomName2}"]))

#---RoomC
def roomC():
  print(random.choice(dialog[f"{scene}{roomName3}"]))

#---RoomD
def RoomD():
  print(random.choice(dialog[f"{scene}{roomName4}"]))

#---RoomE
def RoomE():
  print(random.choice(dialog[f"{scene}{roomName5}"]))


#--------------------------------------- Start of Script

startGame()