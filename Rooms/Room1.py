import random
import json

jsonFileData = "jsonFiles/data.json"
jsonFileDialog = "jsonFiles/dialog.json"
jsonFileBase = "jsonFiles/BaseData.json"
jsonFileRoom = "jsonFiles/randomRoom.json"
jsonFileItem = "jsonFiles/items.json"
jsonInventory = "jsonFiles/inventory.json"

with open(jsonFileItem, 'r') as d:
  global itemsJson
  itemsJson = json.load(d)
with open(jsonFileDialog, 'r') as a:
  global dialog
  dialog = json.load(a)
with open(jsonFileRoom, 'r') as b:
  global roomjson
  roomjson = json.load(b)
with open(jsonFileBase, 'r') as c:
  global baseData
  baseData = json.load(c)
with open(jsonFileData, 'r') as d:
  global data
  data = json.load(d)
with open(jsonInventory, 'r') as e:
  global inventory
  inventory = json.load(e)

SpaceStationPuzzle = [""]
AbandonedHospitalPuzzle = [""]
PrisonPuzzle = [""]
CastlePuzzle = [""]
cabnetcode = random.randint(1000, 9999)

def Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  #
  print(random.choice(dialog[f"{scene}{roomName1}"]))
  currentItems = []
  if scene == "Space Station":
    currentItems = itemsJson["Room1SpaceStationItems"]
  elif scene == "Abandoned Hospital":
    currentItems = itemsJson["Room1AbandonedHospitalItems"]
  elif scene == "Prison":
    currentItems = itemsJson["Room1PrisonItems"]
  elif scene == "Castle":
    currentItems = itemsJson["Room1CastleItems"]


  while True:
    x = random.choice(["item1room1", "item2room1", "item3room1", "item4room1"])
    y = random.choice(["item1room1", "item2room1", "item3room1", "item4room1"])
    if x == y or y == x:
      pass
    else:
      inventory["locations"]["keylocation"] = x
      inventory["locations"]["otherlocation"] = y
      with open(jsonInventory, 'w') as f:
        json.dump(inventory, f, indent=2)
      break

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
        print("storageunit -> Inspect storage unit\nbrokenglass -> inspect broken glass\n\n    --------------------------\n")
        if escapeDoorLocation == "room1":
          print("LockedDoor   -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":
      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
      if inventory["locations"]["keylocation"] == "item1room1":
        if "itemkeyroom1" in inventory["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["pickupkey"]).format("Lock Box key"))
          inventory["items"].append("Lock Box key")
          inventory["unlocks"].append("itemkeyroom1")
      elif inventory["locations"]["otherlocation"] == "item1room1":
        if "itemotherroom1" in inventory["unlocks"]:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a pass code {}", "\n - filler"]).format(cabnetcode))
          inventory["unlocks"].append("itemotherroom1")
        else:
          print(random.choice(dialog["alreadysearched"]))
      else:
        print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[0]))
        inventory["unlocks"].append("item1room1")
      with open(jsonInventory, 'w') as f:
        json.dump(inventory, f, indent=2)
    elif UserInput.lower() == "item2":
      #currentItems[1]
      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
    elif UserInput.lower() == "item3":
      #currentItems[2]
      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
    elif UserInput.lower() == "item4":
      #currentItems[3]
      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
    elif UserInput.lower() == "storageunit":
      print()
    elif UserInput.lower() == "brokenglass":
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