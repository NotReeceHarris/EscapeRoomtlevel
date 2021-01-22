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

def Room4Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  #
  print("\n" + random.choice(dialog[f"{scene}{roomName5}"])) 
  currentItems = []
  if scene == "Space Station":
    currentItems = itemsJson["Room4SpaceStationItems"]
  elif scene == "Abandoned Hospital":
    currentItems = itemsJson["Room4AbandonedHospitalItems"]
  elif scene == "Prison":
    currentItems = itemsJson["Room4PrisonItems"]
  elif scene == "Castle":
    currentItems = itemsJson["Room4CastleItems"]


  with open(jsonInventory, 'r') as e:
      inventoryreset = json.load(e)
  if "keyroom5" in inventoryreset["unlocks"]:
    pass
  else:
    inventoryreset["unlocks"].append("keyroom5")
  with open(jsonInventory, 'w') as f:
    json.dump(inventoryreset, f, indent=2)

  while True:
    x = random.choice(["item1room4", "item2room4", "item3room4", "item4room4"])
    y = random.choice(["item1room4", "item2room4", "item3room4", "item4room4"])
    if x == y or y == x:
      pass
    else:
      with open(jsonInventory, 'r') as e:
        inventoryreset = json.load(e)
      global cabnetcode
      cabnetcode = inventoryreset["code"]["room4cabnet"]
      inventoryreset["locations"]["keylocation"] = x
      inventoryreset["locations"]["otherlocation"] = y
      with open(jsonInventory, 'w') as f:
        json.dump(inventoryreset, f, indent=2)
      break


  while True:
    if specialRoom == roomName4:
      specialRoom = True
    UserInput = input(str(commandLine.format(
        roomName4)))  #The input is put in the varaible UserInput

    if UserInput.lower() == "help":
        print("\n-----------------------------------------\n")
        intd = 0
        for x in currentItems:
            intd += 1
            print(f'item{intd}       -> Inspect {x}')
        print("table       -> Use the Table\n\n    --------------------------\n")
        if escapeDoorLocation == "room4":
          print("lockeddoor   -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":

      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
      if inventoryitem4["locations"]["keylocation"] == "item1room4":
        if "item1room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 4"))
          inventoryitem4["items"].append("Decrypt table part 4")
          inventoryitem4["unlocks"].append("item1room4")
      elif inventoryitem4["locations"]["otherlocation"] == "item1room4":
        if "item1room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 3"))
          inventoryitem4["items"].append("Decrypt table part 3")
          inventoryitem4["unlocks"].append("item1room4")
          inventoryitem4["unlocks"].append("room4paper")
      else:
        if "item1room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[0]))
          inventoryitem4["unlocks"].append("item1room4")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem4, f, indent=2)

    elif UserInput.lower() == "item2":

      #currentItems[1]
      with open(jsonInventory, 'r') as e:
        inventoryitem2 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
      if inventoryitem2["locations"]["keylocation"] == "item2room4":
        if "item2room4" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 4"))
          inventoryitem2["items"].append("Decrypt table part 4")
          inventoryitem2["unlocks"].append("item2room4")
      elif inventoryitem2["locations"]["otherlocation"] == "item2room4":
        if "item2room4" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 3"))
          inventoryitem2["items"].append("Decrypt table part 3")
          inventoryitem2["unlocks"].append("item2room4")
          inventoryitem2["unlocks"].append("room4paper")
      else:
        if "item2room4" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[1]))
          inventoryitem2["unlocks"].append("item2room4")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem2, f, indent=2)

    elif UserInput.lower() == "item3":
      #currentItems[2]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem3 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
      if inventoryitem3["locations"]["keylocation"] == "item3room4":
        if "item3room4" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 4"))
          inventoryitem3["items"].append("Decrypt table part 4")
          inventoryitem3["unlocks"].append("item3room4")
      elif inventoryitem3["locations"]["otherlocation"] == "item3room4":
        if "item3room4" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 3"))
          inventoryitem3["items"].append(f"Decrypt table part 3")
          inventoryitem3["unlocks"].append("item3room4")
          inventoryitem3["unlocks"].append("room4paper")
      else:
        if "item3room4" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[2]))
          inventoryitem3["unlocks"].append("item3room4")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem3, f, indent=2)

    elif UserInput.lower() == "item4":
      #currentItems[3]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
      if inventoryitem4["locations"]["keylocation"] == "item4room4":
        if "item4room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 4"))
          inventoryitem4["items"].append("Decrypt table part 4")
          inventoryitem4["unlocks"].append("item4room4")
      elif inventoryitem4["locations"]["otherlocation"] == "item4room4":
        if "item4room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(dialog["decryptiongraph"]).format("Decrypt table part 4"))
          inventoryitem4["items"].append(f"Decrypt table part 3")
          inventoryitem4["unlocks"].append("item4room4")
          inventoryitem4["unlocks"].append("room4paper")
      else:
        if "item4room4" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[3]))
          inventoryitem4["unlocks"].append("item4room4")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem4, f, indent=2)

    elif UserInput.lower() == "table":

      with open(jsonInventory, 'r') as e:
        inventoryitem5 = json.load(e)


      if "Decrypt table part 1" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 1")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 1")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 2" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 2")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 2")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 3" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 3")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 3")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 4" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 4")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 4")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 5" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 5")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 5")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 6" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 6")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 6")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
      if "Decrypt table part 1" in inventoryitem5["otherdata"]["table"] and "Decrypt table part 2" in inventoryitem5["otherdata"]["table"] and "Decrypt table part 3" in inventoryitem5["otherdata"]["table"] and "Decrypt table part 4" in inventoryitem5["otherdata"]["table"] and "Decrypt table part 5" in inventoryitem5["otherdata"]["table"] and "Decrypt table part 6" in inventoryitem5["otherdata"]["table"]:
        print(random.choice(["So with all the peices together it reads out this", "well i wasnt expecing all the peices to be this", "all the peices together make this table? huh"]))
        table = """
        _________________HOWTO___________________
        Input  >  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
        Output >  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
        _________________________________________
        | . | @ | % | ) | ! | - | = | ^ | * | ; |
        | B | H | L | E | R | U | M | D | Q | F |
        _________________________________________
        | f | c | t | n | q | h | l | x | e | u |
        | Ω | Φ | π | γ | Ψ | ω | Ξ | λ | ζ | μ |
        _________________________________________
        | γ | μ | Φ | Ω | Ψ | Ξ | π | ζ | λ | ω |
        | ! | ; | * | % | . | ^ | ) | - | = | @ |
        _________________________________________
        | 8 | 2 | 7 | 3 | 9 | 1 | 5 | 6 | 4 | 0 |
        | n | x | t | c | u | l | q | e | h | f |
        _________________FINISH__________________
        | H | B | E | D | R | F | M | U | L | Q |
        | 3 | 4 | 8 | 2 | 9 | 5 | 6 | 1 | 7 | 0 |
        """
        print(dialog["clear"])
        print(table)
        input("Press enter to leave table...")
        print(dialog["clear"])
      else:
        print(random.choice(["\nI still need some parts to see the decryption table they might be in the next room\n", "\nmaybe the other peices are in the next room\n", "\nMaybe i should get some more\n", "\nThere are some peices missing maybe i should get somemore\n", "\nI should get some more peices to be able to read this graph\n"]))



      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem5, f, indent=2)

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
      if escapeDoorLocation == "room4":
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