import random
import json

jsonFileData = "jsonFiles/data.json"
jsonFileDialog = "jsonFiles/dialog.json"
jsonFileBase = "jsonFiles/BaseData.json"
jsonFileRoom = "jsonFiles/randomRoom.json"
jsonFileItem = "jsonFiles/items.json"
jsonInventory = "jsonFiles/inventory.json"

with open(jsonFileItem, 'r') as d:
  itemJson = json.load(d)
with open(jsonFileDialog, 'r') as a:
  dialog = json.load(a)
with open(jsonFileRoom, 'r') as b:
  roomjson = json.load(b)
with open(jsonFileBase, 'r') as c:
  baseData = json.load(c)
with open(jsonFileData, 'r') as d:
  data = json.load(d)
with open(jsonInventory, 'r') as e:
  inventory = json.load(e)

SpaceStationPuzzle = [""]
AbandonedHospitalPuzzle = [""]
PrisonPuzzle = [""]
CastlePuzzle = [""]

def Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  lol = random.choice(dialog[f"{scene}{roomName1}"])
  print(lol)
  currentItems = []
  if scene == "Space Station":
    currentItems = itemJson["Room1SpaceStationItems"]
  elif scene == "Abandoned Hospital":
    currentItems = itemJson["Room1AbandonedHospitalItems"]
  elif scene == "Prison":
    currentItems = itemJson["Room1PrisonItems"]
  elif scene == "Castle":
    currentItems = itemJson["Room1CastleItems"]
  while True:

    if specialRoom == roomName1:
        specialRoom = True
    UserInput = input(str(commandLine.format(
        roomName1)))  #The input is put in the varaible UserInput

    if UserInput.lower() == "help":
        print("\n-----------------------------------------\n")
        intd = 0
        for x in currentItems:
            intd += 1
            print(f'item{intd}       -> Inspect {x}')
        print("storageunit -> Inspect storage unit\n\n    --------------------------")
        if escapeDoorLocation == "room1":
          print("LockedDoor  -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":
      #currentItems[0]
      print(random.choice(["You touch the {}, a hair standing fell fills your body"]).filler(currentItems[0]))
    elif UserInput.lower() == "item2":
      #currentItems[1]
      print()
    elif UserInput.lower() == "item3":
      #currentItems[2]
      print()
    elif UserInput.lower() == "item4":
      #currentItems[3]
      print()
    elif UserInput.lower() == "inventory":
        print("\n-----------------------------------------\n")
        for x in inventory["items"]:
            print(x)
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "exit":
        return
    else:
        print(dialog["commandError"])