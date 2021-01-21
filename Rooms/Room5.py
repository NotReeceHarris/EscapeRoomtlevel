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

def Room5Start(mainCharacter, sideCharacter, antagonistCharacter, scene, roomName1, roomName2, roomName3, roomName4, roomName5, specialRoom, inventorySpace, specialItem, commandLine, difficulty, escapeDoorLocation):
  #
  print("\n" + random.choice(dialog[f"{scene}{roomName5}"])) 
  currentItems = []
  if scene == "Space Station":
    currentItems = itemsJson["Room5SpaceStationItems"]
  elif scene == "Abandoned Hospital":
    currentItems = itemsJson["Room5AbandonedHospitalItems"]
  elif scene == "Prison":
    currentItems = itemsJson["Room5PrisonItems"]
  elif scene == "Castle":
    currentItems = itemsJson["Room5CastleItems"]


  while True:
    x = random.choice(["item1room5", "item2room5", "item3room5", "item4room5"])
    y = random.choice(["item1room5", "item2room5", "item3room5", "item4room5"])
    if x == y or y == x:
      pass
    else:
      with open(jsonInventory, 'r') as e:
        inventoryreset = json.load(e)
      global cabnetcode
      cabnetcode = inventoryreset["code"]["room5cabnet"]
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
        print("\n-----------------------------------------\n")
        intd = 0
        for x in currentItems:
            intd += 1
            print(f'item{intd}       -> Inspect {x}')
        print("vault       -> Inspect Vault\n\n    --------------------------\n")
        if escapeDoorLocation == "room5":
          print("lockeddoor   -> Door")
        print(
            "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
        )
        print("\n-----------------------------------------\n")
    elif UserInput.lower() == "item1":

      with open(jsonInventory, 'r') as e:
        inventoryitem1 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
      if inventoryitem1["locations"]["keylocation"] == "item1room5":
        if "item1room5" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice([dialog["decryptiongraph"]]).format("Decrypt table part 5"))
          inventoryitem1["items"].append("Decrypt table part 5")
          inventoryitem1["unlocks"].append("item1room5")
      elif inventoryitem1["locations"]["otherlocation"] == "item1room5":
        if "item1room5" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 6"))
          inventoryitem1["items"].append("Decrypt table part 6")
          inventoryitem1["unlocks"].append("item1room5")
          inventoryitem1["unlocks"].append("room5paper")
      else:
        if "item1room5" in inventoryitem1["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[0]))
          inventoryitem1["unlocks"].append("item1room5")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem1, f, indent=2)

    elif UserInput.lower() == "item2":

      #currentItems[1]
      with open(jsonInventory, 'r') as e:
        inventoryitem2 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
      if inventoryitem2["locations"]["keylocation"] == "item2room5":
        if "item2room5" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice([dialog["decryptiongraph"]]).format("Decrypt table part 5"))
          inventoryitem2["items"].append("Decrypt table part 5")
          inventoryitem2["unlocks"].append("item2room5")
      elif inventoryitem2["locations"]["otherlocation"] == "item2room5":
        if "item2room5" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 6"))
          inventoryitem2["items"].append("Decrypt table part 6")
          inventoryitem2["unlocks"].append("item2room5")
          inventoryitem2["unlocks"].append("room5paper")
      else:
        if "item2room5" in inventoryitem2["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[1]))
          inventoryitem2["unlocks"].append("item2room5")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem2, f, indent=2)

    elif UserInput.lower() == "item3":
      #currentItems[2]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem3 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
      if inventoryitem3["locations"]["keylocation"] == "item3room5":
        if "item3room5" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice([dialog["decryptiongraph"]]).format("Decrypt table part 5"))
          inventoryitem3["items"].append("Decrypt table part 5")
          inventoryitem3["unlocks"].append("item3room5")
      elif inventoryitem3["locations"]["otherlocation"] == "item3room5":
        if "item3room5" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 6"))
          inventoryitem3["items"].append("Decrypt table part 6")
          inventoryitem3["unlocks"].append("item3room5")
          inventoryitem3["unlocks"].append("room5paper")
      else:
        if "item3room5" in inventoryitem3["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[2]))
          inventoryitem3["unlocks"].append("item3room5")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem3, f, indent=2)

    elif UserInput.lower() == "item4":
      #currentItems[3]
      
      with open(jsonInventory, 'r') as e:
        inventoryitem4 = json.load(e)

      print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
      if inventoryitem4["locations"]["keylocation"] == "item4room5":
        if "item4room5" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice([dialog["decryptiongraph"]]).format("Decrypt table part 5"))
          inventoryitem4["items"].append("Decrypt table part 5")
          inventoryitem4["unlocks"].append("item4room5")
      elif inventoryitem4["locations"]["otherlocation"] == "item4room5":
        if "item4room5" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n- A peice of paper? its all wet, but i can only just see a passcode {}", "\n - Paper? maybe it has someth... a number {} i should remember this."]).format("Decrypt table part 6"))
          inventoryitem4["items"].append("Decrypt table part 6")
          inventoryitem4["unlocks"].append("item4room5")
          inventoryitem4["unlocks"].append("room5paper")
      else:
        if "item4room5" in inventoryitem4["unlocks"]:
          print(random.choice(dialog["alreadysearched"]))
        else:
          print(random.choice(["\n - There is nothing here its just a {}", "\n - Maybe there is nothing to this {}, its just bare."]).format(currentItems[3]))
          inventoryitem4["unlocks"].append("item4room5")

      with open(jsonInventory, 'w') as f:
        json.dump(inventoryitem4, f, indent=2)

    elif UserInput.lower() == "vault":

      with open(jsonInventory, 'r') as e:
        inventoryitem5 = json.load(e)

      decrypt = ""

      if difficulty == 1:
        for x in inventoryitem5["code"]["dif1num"].split(" "):
          if x == 0:
            decrypt = decrypt + str(7)
          if x == 1:
            decrypt = decrypt + str(2)
          if x == 2:
            decrypt = decrypt + str(6)
          if x == 3:
            decrypt = decrypt + str(0)
          if x == 4:
            decrypt = decrypt + str(3)
          if x == 5:
            decrypt = decrypt + str(4)
          if x == 6:
            decrypt = decrypt + str(1)
          if x == 7:
            decrypt = decrypt + str(8)
          if x == 8:
            decrypt = decrypt + str(9)
          if x == 9:
            decrypt = decrypt + str(5)
      elif difficulty == 2:
        for x in inventoryitem5["code"]["dif2num"].split(" "):
          if x == 0:
            decrypt = decrypt + str(7)
          if x == 1:
            decrypt = decrypt + str(2)
          if x == 2:
            decrypt = decrypt + str(6)
          if x == 3:
            decrypt = decrypt + str(0)
          if x == 4:
            decrypt = decrypt + str(3)
          if x == 5:
            decrypt = decrypt + str(4)
          if x == 6:
            decrypt = decrypt + str(1)
          if x == 7:
            decrypt = decrypt + str(8)
          if x == 8:
            decrypt = decrypt + str(9)
          if x == 9:
            decrypt = decrypt + str(5)
      elif difficulty == 3:
        for x in inventoryitem5["code"]["dif3num"].split(" "):
          if x == 0:
            decrypt = decrypt + str(7)
          if x == 1:
            decrypt = decrypt + str(2)
          if x == 2:
            decrypt = decrypt + str(6)
          if x == 3:
            decrypt = decrypt + str(0)
          if x == 4:
            decrypt = decrypt + str(3)
          if x == 5:
            decrypt = decrypt + str(4)
          if x == 6:
            decrypt = decrypt + str(1)
          if x == 7:
            decrypt = decrypt + str(8)
          if x == 8:
            decrypt = decrypt + str(9)
          if x == 9:
            decrypt = decrypt + str(5)
      
      if "vault" in inventoryitem5["unlocks"]:
        print(random.choice(["So there is a number in the vault it says {}", "Right it says {} i wonder what it means", ""]).format(decrypt))
        
      else:
        print(random.choice(["\nThe vault looks like it has stuff etched into it it says {}, maybe this is the code huh simple\n", "Is that a number? wait no its etched into the vault huh it says.. {}"]).format(decrypt))






      if "Decrypt table part 1" in inventoryitem5["items"]:
        inventoryitem5["items"].remove("Decrypt table part 1")
        inventoryitem5["otherdata"]["table"].append("Decrypt table part 1")
        print(random.choice(["You put the peice on the table, Lets hope it matches the others", "You place the peice on the table, Lets hope it matches the others", "Il put this peice on the table maybe the others are in the next room"]))
        











      else:
        print(random.choice(["Maybe i should go finish off the decryption table", "Huh maybe the decryption table will help me"]))
      
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
        return
    elif UserInput.lower() == "lockeddoor":
      if escapeDoorLocation == "room5":
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