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

def Room3Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  #
  print("\n" + random.choice(dialog[f"{scene}{roomName3}"])) 
  currentItems = []
  if scene == "Space Station":
    currentItems = itemsJson["Room3SpaceStationItems"]
  elif scene == "Abandoned Hospital":
    currentItems = itemsJson["Room3AbandonedHospitalItems"]
  elif scene == "Prison":
    currentItems = itemsJson["Room3PrisonItems"]
  elif scene == "Castle":
    currentItems = itemsJson["Room3CastleItems"]
    
  while True:
    x = random.choice(["item1room3", "item2room3", "item3room3", "item4room3"])
    y = random.choice(["item1room3", "item2room3", "item3room3", "item4room3"])
    if x == y or y == x:
      pass
    else:
      with open(jsonInventory, 'r') as e:
        inventoryreset = json.load(e)
      global cabnetcode
      cabnetcode = inventoryreset["code"]["room3cabnet"]
      inventoryreset["locations"]["keylocation"] = x
      inventoryreset["locations"]["otherlocation"] = y
      with open(jsonInventory, 'w') as f:
        json.dump(inventoryreset, f, indent=2)
    break

  while True:
    if specialRoom == roomName1:
      specialRoom = True
    UserInput = input(str(commandLine.format(
        roomName3)))  #The input is put in the varaible UserInput

    if UserInput.lower() == "help":
        print("\n-----------------------------------------\n")
        intd = 0
        for x in currentItems:
            intd += 1
            print(f'item{intd}       -> Inspect {x}')
        print("skull       -> Inspect skull\n\n    --------------------------\n")
        if escapeDoorLocation == "room3":
          print("lockeddoor   -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":

      with open(jsonInventory, 'r') as e:
        inventoryitem1 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
      if inventoryitem1["locations"]["keylocation"] == "item1room3":
        if "item1room3" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["Whats this a peice of paper, it has scribbles all over it, wait there something on the back '{}' does this mean something", "scribbles? who did this, is it ment to be art?, wait it says '{}' on the back"]).format("Decrypt table part 1"))
          inventoryitem1["items"].append("Decrypt table part 1")
          inventoryitem1["unlocks"].append("item1room3")
      elif inventoryitem1["locations"]["otherlocation"] == "item1room3":
        if "item1room3" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["Whats this a peice of paper, it has scribbles all over it, wait there something on the back '{}' does this mean something", "scribbles? who did this, is it ment to be art?, wait it says '{}' on the back"]).format("Decrypt table part 2"))
          inventoryitem1["items"].append(f"Decrypt table part 2")
          inventoryitem1["unlocks"].append("item1room3")
          inventoryitem1["unlocks"].append("room3paper")
      else:
        if "item1room3" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[0]))
          inventoryitem1["unlocks"].append("item1room3")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem1, f, indent=2)

    elif UserInput.lower() == "item2":

      #currentItems[1]
      with open(jsonInventory, 'r') as e:
        inventoryitem2 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
      if inventoryitem2["locations"]["keylocation"] == "item2room3":
        if "item2room3" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["Whats this a peice of paper, it has scribbles all over it, wait there something on the back '{}' does this mean something", "scribbles? who did this, is it ment to be art?, wait it says '{}' on the back"]).format("Decrypt table part 1"))
          inventoryitem2["items"].append("Decrypt table part 1")
          inventoryitem2["unlocks"].append("item2room3")
      elif inventoryitem2["locations"]["otherlocation"] == "item2room3":
        if "item2room3" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 2"))
          inventoryitem2["items"].append("Decrypt table part 2")
          inventoryitem2["unlocks"].append("item2room3")
          inventoryitem2["unlocks"].append("room3paper")
      else:
        if "item2room3" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[1]))
          inventoryitem2["unlocks"].append("item2room3")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem2, f, indent=2)

    elif UserInput.lower() == "item3":
      #currentItems[2]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem3 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
      if inventoryitem3["locations"]["keylocation"] == "item3room3":
        if "item3room3" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["Whats this a peice of paper, it has scribbles all over it, wait there something on the back '{}' does this mean something", "scribbles? who did this, is it ment to be art?, wait it says '{}' on the back"]).format("Decrypt table part 1"))
          inventoryitem3["items"].append("Decrypt table part 1")
          inventoryitem3["unlocks"].append("item3room3")
      elif inventoryitem3["locations"]["otherlocation"] == "item3room3":
        if "item3room3" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 2"))
          inventoryitem3["items"].append("Decrypt table part 2")
          inventoryitem3["unlocks"].append("item3room3")
          inventoryitem3["unlocks"].append("room3paper")
      else:
        if "item3room3" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[2]))
          inventoryitem3["unlocks"].append("item3room3")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem3, f, indent=2)

    elif UserInput.lower() == "item4":
      #currentItems[3]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
      if inventoryitem4["locations"]["keylocation"] == "item4room3":
        if "item4room3" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["Whats this a peice of paper, it has scribbles all over it, wait there something on the back '{}' does this mean something", "scribbles? who did this, is it ment to be art?, wait it says '{}' on the back"]).format("Decrypt table part 1"))
          inventoryitem4["items"].append("Decrypt table part 1")
          inventoryitem4["unlocks"].append("item4room3")
      elif inventoryitem4["locations"]["otherlocation"] == "item4room3":
        if "item4room3" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 2"))
          inventoryitem4["items"].append("Decrypt table part 2")
          inventoryitem4["unlocks"].append("item4room3")
          inventoryitem4["unlocks"].append("room3paper")
      else:
        if "item4room3" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[3]))
          inventoryitem4["unlocks"].append("item4room3")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem4, f, indent=2)

    elif UserInput.lower() == "skull":
      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)
      if "skull" in inventoryitem4["unlocks"]:
        print(random.choice(["right it says {} on it i should remember it!", "it has {} carved into it i have already seen this", "iv already seen this it says {} on it"]).format(inventoryitem4["code"]["room4cabnet"]))
      else:
        print(random.choice(["ah finally something simple it says {} on the top of it", "damn who carved {} into it", "i should remeber this carving {}"]).format(inventoryitem4["code"]["room4cabnet"]))

    elif UserInput.lower() == "inventory":
      with open(jsonInventory, 'r') as e:
        inventoryshow = json.load(e)
        print("\n-----------------------------------------\n")
        for x in inventoryshow["items"]:
            print(x)
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "exit":
        print(dialog["clear"])
        return
    elif UserInput.lower() == "lockeddoor":
      if escapeDoorLocation == "room3":
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