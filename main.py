# --------------------------------------- Imports

import random
import time
import json
from Rooms import Room1, Room2, Room3, Room4, Room5
from calculate import cal

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

# --------------------------------------- Start Function

def startGame():

  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  skullnum1 = random.randint(0, 9)
  skullnum2 = random.randint(0, 9)
  skullnum3 = random.randint(0, 9)
  skullnum4 = random.randint(0, 9)
  skullnum5 = random.randint(0, 9)

  resetinventory = {
    "items": ["Key (Room 1)"],
    "randomItems": [],
    "unlocks": [],
    "locations": {
      "keylocation": "",
      "otherlocation": ""
    },
    "code":{
      "room1cabnet": random.randint(1000, 9999),
      "room2cabnet": random.randint(1000, 9999),
      "room3cabnet": f"{skullnum1} {skullnum2} {skullnum3} {skullnum4} {skullnum5}",
      "room4cabnet": f"{skullnum1}{skullnum2}{skullnum3}{skullnum4}{skullnum5}",
      "dif1num": f"{random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)}",
      "dif2num": f"{random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)}",
      "dif3num": f"{random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)}"
    },
    "timestart": int(time.time()),
    "otherdata": {
      "room2": [],
      "table": [],
      "difficulty": 0
    }
    }
  
  inventoryreset.update(resetinventory)

  with open(jsonInventory, 'w') as f:
    json.dump(inventoryreset, f, indent=2)

  if data["Debug"]:
    print(dialog["debug"].format(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, inventorySpace, specialItem, specialRoom, escapeDoorLocation))
  while True:
    with open(jsonInventory, 'r') as a:
      inventoryreset = json.load(a)
    difficultyinput = input("-----------------------------------------\nSelect a difficulty(1, 2, 3)\n-----------------------------------------\n >#>")
    if difficultyinput == "1":
      inventoryreset["otherdata"]["difficulty"] = 1
      break
    elif difficultyinput == "2":
      inventoryreset["otherdata"]["difficulty"] = 2
      break
    elif difficultyinput == "3":
      inventoryreset["otherdata"]["difficulty"] = 3
      break
    else:
      print("Please Input a valid difficulty!")
    with open(jsonInventory, 'w') as f:
      json.dump(inventoryreset, f, indent=2)
  allcalc = cal()
  allposs = allcalc['allposs']
  allvars = allcalc['allvar']
  alllines = allcalc['lines']
  allperc = allcalc['perc']
  allpossf = f"{allposs:,}"
  allvarsf = f"{allvars:,}"
  alllinesf = f"{alllines:,}"

  print(dialog["start"].format(allpossf, allvarsf, alllinesf, inventoryreset["otherdata"]["difficulty"], allperc, allpossf, allvarsf, alllinesf))
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
    with open(jsonInventory, 'r') as e:
      inventoryshow = json.load(e)
    userInput = input(str(commandLine.format('Outer Rooms')))
    if userInput.lower() == "help":
      print(dialog["spacer"])
      print(f"room1        ->  {roomName1}\nroom2        ->  {roomName2}\nroom3        ->  {roomName3}\nroom4        ->  {roomName4}\nroom5        ->  {roomName5}\n\n    --------------------------\n\nhelp         ->  Help Menu\ninventory    -> Show inventory")
      print(dialog["spacer"])
    elif userInput.lower() == "room1":
      if "Key (Room 1)" in inventoryshow["items"]:
        roomA()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room2":
      if "Key (Room 2)" in inventoryshow["items"]:
        roomB()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room3":
      if "Key (Room 3)" in inventoryshow["items"]:
        roomC()
      else:
        print(random.choice(["You try to open the door, it rattles. you need a key!", "Theres a key hole, maybe you need a key for this room", "This door wont budge without a key!"]))
    elif userInput.lower() == "room4":
      print(random.choice(["\nOh this doesnt need a key theres a keypad!", "\nfiller"]))
      while True:
        with open(jsonInventory, 'r') as e:
          inventoryshow = json.load(e)
        userinput01 = input("\nEnter passcode\n>#> ")
        if not userinput01.isnumeric():
          print(random.choice(["\nThis keypad only has numbers, not letters.", "\nHuh? I dont see a letter here", "\nMaybe its a number there are no numbers here"]))
        elif str(userinput01) == str(inventoryshow["code"]["room4cabnet"]):
          print("\nHuh it worked...\n", "\nWow....I'm really good at guessing this, aren't I?\n", "\nSo this is the power of completely guessing a keypad sequence?\n")
          roomD()
        else:
          print(random.choice(["\nThe number entered was incorrect.", "\nAccess Denied.", "\nAunauthroized Access Code", "\nDamn it's the wrong code.", "\nSeriously?", "\nThis is a joke.", "\nGod damn it! We are almost out!", "\nHow many times will I get this wrong?", "\nCome on! Hurry it up!"]))
        break

    elif userInput.lower() == "room5":
      with open(jsonInventory, 'r') as e:
        inventoryshow = json.load(e)
      if "keyroom5" in inventoryshow["unlocks"]:
        roomE()
      else:
        print("\nThere doesnt seem to be a lock, maybe its jammed i should go check the other rooms\n", "\nmaybe its stuck i should go check the other rooms and figure this out later\n", "\nhuh its stuck maybe i should go check the other rooms and come back later\n")
    elif userInput.lower() == "inventory":
        with open(jsonInventory, 'r') as e:
          inventoryshow = json.load(e)
        print("\n-----------------------------------------\n")
        for x in inventoryshow["items"]:
            print(x)
        print("\n-----------------------------------------\n")
    else:
      print(f'{dialog["spacer"]}Invalid command try "help".{dialog["spacer"]}')
  


# --------------------------------------- Corridor Function

def Corridor():
  print()

#---RoomA
def roomA():
  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  difficulty = inventoryreset["otherdata"]["difficulty"]
  Room1.Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomB
def roomB():
  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  difficulty = inventoryreset["otherdata"]["difficulty"]
  Room2.Room2Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomC
def roomC():
  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  difficulty = inventoryreset["otherdata"]["difficulty"]
  Room3.Room3Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomD
def roomD():
  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  difficulty = inventoryreset["otherdata"]["difficulty"]
  print(random.choice(dialog[f"{scene}{roomName4}"]))
  Room4.Room4Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in

#---RoomE
def roomE():
  with open(jsonInventory, 'r') as a:
    inventoryreset = json.load(a)
  difficulty = inventoryreset["otherdata"]["difficulty"]
  print(random.choice(dialog[f"{scene}{roomName5}"]))
  Room5.Room5Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation) #all the data that the room will need is parsed in


#--------------------------------------- Start of Script

startGame()