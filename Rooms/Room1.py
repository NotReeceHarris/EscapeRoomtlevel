import random
import json
import time
import sys  

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

def Room1Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  #
  print("\n" + random.choice(dialog[f"{scene}{roomName1}"])) 
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
      with open(jsonInventory, 'r') as e:
        inventoryreset = json.load(e)
      global cabnetcode
      cabnetcode = inventoryreset["code"]["room1cabnet"]
      inventoryreset["locations"]["keylocation"] = x
      inventoryreset["locations"]["otherlocation"] = y
      with open(jsonInventory, 'w') as f:
        json.dump(inventoryreset, f, indent=2)
      break

  while True:

    if specialRoom == roomName1:
      specialRoom = True
    UserInput = input(str(commandLine.format(
        roomName1)))  #The input is put in the varaible UserInput

    if UserInput.lower() == "help":
        print(dialog["clear"])
        print("\n-----------------------------------------\n")
        intd = 0
        for x in currentItems:
            intd += 1
            print(f'item{intd}       -> Inspect {x}')
        print("storageunit -> Inspect storage unit\n\n    --------------------------\n")
        if escapeDoorLocation == "room1":
          print("lockeddoor   -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":
      print(dialog["clear"])
      with open(jsonInventory, 'r') as e:
        inventoryitem1 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
      if inventoryitem1["locations"]["keylocation"] == "item1room1":
        if "item1room1" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["pickupkey"]).format("Key (Room1 LockBox)"))
          inventoryitem1["items"].append("Key (Room1 LockBox)")
          inventoryitem1["unlocks"].append("item1room1")
      elif inventoryitem1["locations"]["otherlocation"] == "item1room1":
        if "item1room1" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format(cabnetcode))
          inventoryitem1["items"].append(f"Paper ({cabnetcode})")
          inventoryitem1["unlocks"].append("item1room1")
          inventoryitem1["unlocks"].append("room1paper")
      else:
        if "item1room1" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[0]))
          inventoryitem1["unlocks"].append("item1room1")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem1, f, indent=2)

    elif UserInput.lower() == "item2":
      print(dialog["clear"])
      #currentItems[1]
      with open(jsonInventory, 'r') as e:
        inventoryitem2 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
      if inventoryitem2["locations"]["keylocation"] == "item2room1":
        if "item2room1" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["pickupkey"]).format("Key (Room1 LockBox)"))
          inventoryitem2["items"].append("Key (Room1 LockBox)")
          inventoryitem2["unlocks"].append("item2room1")
      elif inventoryitem2["locations"]["otherlocation"] == "item2room1":
        if "item2room1" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format(cabnetcode))
          inventoryitem2["items"].append(f"Paper ({cabnetcode})")
          inventoryitem2["unlocks"].append("item2room1")
          inventoryitem2["unlocks"].append("room1paper")
      else:
        if "item2room1" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[1]))
          inventoryitem2["unlocks"].append("item2room1")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem2, f, indent=2)

    elif UserInput.lower() == "item3":
      print(dialog["clear"])
      #currentItems[2]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem3 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
      if inventoryitem3["locations"]["keylocation"] == "item3room1":
        if "item3room1" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["pickupkey"]).format("Key (Room1 LockBox)"))
          inventoryitem3["items"].append("Key (Room1 LockBox)")
          inventoryitem3["unlocks"].append("item3room1")
      elif inventoryitem3["locations"]["otherlocation"] == "item3room1":
        if "item3room1" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format(cabnetcode))
          inventoryitem3["items"].append(f"Paper ({cabnetcode})")
          inventoryitem3["unlocks"].append("item3room1")
          inventoryitem3["unlocks"].append("room1paper")
      else:
        if "item3room1" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[2]))
          inventoryitem3["unlocks"].append("item3room1")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem3, f, indent=2)

    elif UserInput.lower() == "item4":
      print(dialog["clear"])
      #currentItems[3]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
      if inventoryitem4["locations"]["keylocation"] == "item4room1":
        if "item4room1" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["pickupkey"]).format("Key (Room1 LockBox)"))
          inventoryitem4["items"].append("Key (Room1 LockBox)")
          inventoryitem4["unlocks"].append("item4room1")
      elif inventoryitem4["locations"]["otherlocation"] == "item4room1":
        if "item4room1" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format(cabnetcode))
          inventoryitem4["items"].append(f"Paper ({cabnetcode})")
          inventoryitem4["unlocks"].append("item4room1")
          inventoryitem4["unlocks"].append("room1paper")
      else:
        if "item4room1" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[3]))
          inventoryitem4["unlocks"].append("item4room1")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem4, f, indent=2)

    elif UserInput.lower() == "storageunit":
      print(dialog["clear"])
      with open(jsonInventory, 'r') as e:
        inventoryitem5 = json.load(e)

      if "Key (Room1 LockBox)" in inventoryitem5["items"] or "boxopenedroom1" in inventoryitem5["unlocks"]:
        if "boxopenedroom1" in inventoryitem5["unlocks"] and "room1paper" not in inventoryitem5["unlocks"]:
          print(random.choice(["\nRight this lock box needs a code", "\nmaybe i have the code", "\nMaybe the code is on a note."]))
        elif "boxopenedroom1" not in inventoryitem5["unlocks"] and "room1paper" not in inventoryitem5["unlocks"]:
          print(random.choice(["\nA lockbox? huh is it open! I need a 4 digit code", "\nWhy is there only a little lockbox in this huge Storage unit, Theres a 4 digit lock on it!"]))
          inventoryitem5["unlocks"].append("boxopenedroom1")
        elif "boxopenedroom1" in inventoryitem5["unlocks"] and "room1paper" not in inventoryitem5["unlocks"]:
          print(random.choice(["\nI have already opend this box, its just a waste of time", "\nHavent i already opend this box? if so it would be a waste of time to open again.", "\nI have already taken stuff from here it would be pointless to look at it again."]))
        else:
          if "room1paper" in inventoryitem5["unlocks"] and "Key (Room 2)" not in inventoryitem5["items"]:
            print(random.choice(["\nYou use the code {}, it opens there is a key that says\n\"Room 2\" on it and a weird looking torch", "\nYou enter the code {}, it unlocks! theres a key that says\n\"Room 2\" on it and a wierd looking torch"]).format(cabnetcode))
            inventoryitem5["items"].append("Black Light")
            inventoryitem5["items"].append("Key (Room 2)")
            inventoryitem5["unlocks"].append("room1lockbox")
          elif "Key (Room 2)" in inventoryitem5["items"]:
            print(random.choice(["\nI have already opend this box, its just a waste of time", "\nHavent i already opend this box? if so it would be a waste of time to open again.", "\nI have already taken stuff from here it would be pointless to look at it again."]))
          else:
            print(random.choice(["\nA lockbox? huh is it open! I need a 4 digit code", "\nWhy is there only a little lockbox in this huge Storage unit, Theres a 4 digit lock on it!"]))
          
        
      else:
        print(random.choice(["\nTheres a lock, maybe theres a key around here", "\nIts locked, maybe a key is around here", "\nA lock? whats hidden in here, maybe a key would tell me", "\nWell im not getting into this maybe i need a key"]))

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem5, f, indent=2)

    elif UserInput.lower() == "inventory":
      with open(jsonInventory, 'r') as e:
        inventoryshow = json.load(e)
        print(dialog["clear"])
        print("\n-----------------------------------------\n")
        for x in inventoryshow["items"]:
            print(x)
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "exit":
        print(dialog["clear"])
        return
    elif UserInput.lower() == "lockeddoor":
      if escapeDoorLocation == "room1":
        with open(jsonInventory, 'r') as e:
          inventoryshow = json.load(e)
        if "Key (Exit)" in inventoryshow["items"]:
          timestamp = int(time.time()) - inventoryshow["timestart"]
          dt_object = f"{round(timestamp / 60, 2)} Minutes"
          currenttime = time.ctime(time.time())
          print(dialog["escapewin"].format(scene, sideCharacter, antagonistCharacter, currenttime, dt_object))
          time.sleep(10)
          sys.exit()
        else:
          print(random.choice(["\nIts locked!, maybe i could find a key somewhere", "\nIts locked, I need a key", "\nIts locked, maybe i can kick the door down\n*You try to kick the door down*\nIt wont budge, Maybe i have to find a key for it."]))
      else:
        print(dialog["commandError"])
    else:
        print(dialog["commandError"])