# --------------------------------------- Imports

import random
import time
from inventorySystem import SeeI, AddI, DropI
import json
from Rooms import Room1, Room2, Room3, Room4, Room5

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
difficulty = 0

# --------------------------------------- Start Function

def startGame():
  while True:
    global difficulty
    difficultyinput = input("-----------------------------------------\nSelect a difficulty(1, 2, 3)\n-----------------------------------------\n >#>")
    if difficultyinput == "1":
      difficulty += 1
      break
    elif difficultyinput == "2":
      difficulty += 2
      break
    elif difficultyinput == "3":
      difficulty += 3
      break
    else:
      print("Please Input a valid difficulty!")

  if data["Debug"]:
    print(dialog["debug"].format(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, inventorySpace, specialItem, specialRoom))
  print(dialog["start"].format(difficulty))
  input('\nPress Enter to start...')
  global Start
  Start = time.time()
  print(dialog["dialog1.0"])
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
  print(dialog["dialog1.16"].format(sideCharacter))
  input()
  print(dialog["dialog1.17"].format(sideCharacter))
  input()


  while True:
    userInput = input(str(commandLine.format('Outer Rooms')))
    commandlist = ["room1        ->  Enter Room 1", "room2        ->  Enter Room 1", "room3        ->  Enter Room 1", "room4        ->  Enter Room 1", "room5        ->  Enter Room 1", "inventory    ->  Display Inventory"]
    if userInput.lower() == "help":
      print(dialog["spacer"])
      for i in commandlist:
        print(i)
      print(dialog["spacer"])
    elif userInput.lower() == "room1":
      roomA()
    else:
      print(f'{dialog["spacer"]}Invalid command try "help".{dialog["spacer"]}')
  


# --------------------------------------- Corridor Function

def Corridor():
  print()

#---RoomA
def roomA():
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty) #all the data that the room will need is parsed in

#---RoomB
def roomB():
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty) #all the data that the room will need is parsed in

#---RoomC
def roomC():
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty) #all the data that the room will need is parsed in

#---RoomD
def RoomD():
  print(random.choice(dialog[f"{scene}{roomName4}"]))
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty) #all the data that the room will need is parsed in

#---RoomE
def RoomE():
  print(random.choice(dialog[f"{scene}{roomName5}"]))
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty) #all the data that the room will need is parsed in


#--------------------------------------- Start of Script

startGame()