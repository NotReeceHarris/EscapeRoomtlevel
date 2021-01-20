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
jsonInventory = "jsonFiles/inventory.json"

with open(jsonFileDialog, 'r') as a:
  dialog = json.load(a)
with open(jsonFileRoom, 'r') as b:
  roomjson = json.load(b)
with open(jsonFileBase, 'r') as c:
  baseData = json.load(c)
with open(jsonFileData, 'r') as d:
  data = json.load(d)
with open(jsonInventory, 'r') as a:
  inventory = json.load(a)

mainCharacter = random.choice(baseData["mainCharacterNames"])
sideCharacter = random.choice(baseData["sideCharacterNames"])
antagonistCharacter = random.choice(baseData["antagonistNames"])
scene = random.choice(baseData["Scene"])
roomName1 = random.choice(roomjson[f'{scene}1'])
roomName2 = random.choice(roomjson[f'{scene}2'])
roomName3 = random.choice(roomjson[f'{scene}3'])
roomName4 = random.choice(roomjson[f'{scene}4'])
roomName5 = random.choice(roomjson[f'{scene}5'])
escapeDoorLocation = random.choice(["room1", "room2", "room3", "room4", "room4"])
specialRoom = random.choice([roomName1, roomName2, roomName3, roomName4, roomName5])
inventorySpace = data["inventorySpace"]
specialItem = random.choice(baseData[f"{scene}SpecialItem"])
commandLine = '\nRoom: {}  |  Commands: Help, Inventory\n >#> '
difficulty = 0

# --------------------------------------- Start Function

def startGame():
  if data["Debug"]:
    print(dialog["debug"].format(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, inventorySpace, specialItem, specialRoom, escapeDoorLocation))
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
  corridor()

def corridor():
  while True:
    userInput = input(str(commandLine.format('Outer Rooms')))
    if userInput.lower() == "help":
      print(dialog["spacer"])
      print(f"room1        ->  {roomName1}\nroom2        ->  {roomName2}\nroom3        ->  {roomName3}\nroom4        ->  {roomName4}\nroom5        ->  {roomName5}\nhelp         ->  Help Menu\ninventory    -> Show inventory")
      print(dialog["spacer"])
    elif userInput.lower() == "room1":
      if "room1key" in inventory["items"]:
        roomA()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room2":
      if "room2key" in inventory["items"]:
        roomB()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room3":
      if "room3key" in inventory["items"]:
        roomC()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room4":
      if "room4key" in inventory["items"]:
        roomD()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room5":
      if "room5key" in inventory["items"]:
        roomE()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    else:
      print(f'{dialog["spacer"]}Invalid command try "help".{dialog["spacer"]}')
  


# --------------------------------------- Corridor Function

def Corridor():
  print()

#---RoomA
def roomA():
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomB
def roomB():
  Room2.Room2Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomC
def roomC():
  Room3.Room3Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomD
def roomD():
  print(random.choice(dialog[f"{scene}{roomName4}"]))
  Room4.Room4Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomE
def roomE():
  print(random.choice(dialog[f"{scene}{roomName5}"]))
  Room5.Room5Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in


#--------------------------------------- Start of Script

startGame()