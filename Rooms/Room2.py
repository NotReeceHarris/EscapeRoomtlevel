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

with open(jsonFileItem, "r") as d:
    global itemsJson
    itemsJson = json.load(d)
with open(jsonFileDialog, "r") as a:
    global dialog
    dialog = json.load(a)
with open(jsonFileRoom, "r") as b:
    global roomjson
    roomjson = json.load(b)
with open(jsonFileBase, "r") as c:
    global baseData
    baseData = json.load(c)
with open(jsonFileData, "r") as d:
    global data
    data = json.load(d)
with open(jsonInventory, "r") as e:
    global inventory
    inventory = json.load(e)

SpaceStationPuzzle = [""]
AbandonedHospitalPuzzle = [""]
PrisonPuzzle = [""]
CastlePuzzle = [""]


def Room2Start(
    mainCharacter,
    sideCharacter,
    antagonistCharacter,
    scene,
    roomName1,
    roomName2,
    roomName3,
    roomName4,
    roomName5,
    specialRoom,
    inventorySpace,
    specialItem,
    commandLine,
    difficulty,
    escapeDoorLocation,
):

    #

    with open(jsonInventory, "r") as e:
        inventoryitem5 = json.load(e)

    print1 = random.randint(0, 9)
    print2 = random.randint(0, 9)
    print3 = random.randint(0, 9)
    print4 = random.randint(0, 9)
    inventoryitem5["code"]["room2cabnet"] = f"{print1}{print2}{print3}{print4}"
    inventoryitem5["otherdata"]["room2"] = [print4, print1, print2, print3]

    with open(jsonInventory, "w") as f:
        json.dump(inventoryitem5, f, indent=2)

    print(f"\n{random.choice(dialog[f'{scene}{roomName2}'])}")
    currentItems = []
    if scene == "Space Station":
        currentItems = itemsJson["Room2SpaceStationItems"]
    elif scene == "Abandoned Hospital":
        currentItems = itemsJson["Room2AbandonedHospitalItems"]
    elif scene == "Prison":
        currentItems = itemsJson["Room2PrisonItems"]
    elif scene == "Castle":
        currentItems = itemsJson["Room2CastleItems"]

    while True:
        x = random.choice(["item1room2", "item2room2", "item3room2", "item4room2"])
        y = random.choice(["item1room2", "item2room2", "item3room2", "item4room2"])
        if x == y or y == x:
            pass
        else:
            with open(jsonInventory, "r") as e:
                inventoryreset = json.load(e)
            global cabnetcode
            cabnetcode = inventoryreset["code"]["room2cabnet"]
            inventoryreset["locations"]["keylocation"] = x
            inventoryreset["locations"]["otherlocation"] = y
            with open(jsonInventory, "w") as f:
                json.dump(inventoryreset, f, indent=2)
            break

    while True:

        if specialRoom == roomName1:
            specialRoom = True
        UserInput = input(
            str(commandLine.format(roomName2))
        )  # The input is put in the varaible UserInput

        if UserInput.lower() == "help":
            with open(jsonInventory, "r") as e:
                inventoryitem1 = json.load(e)
                print(dialog["clear"])
                print("\n-----------------------------------------\n")
                intd = 0
                for x in currentItems:
                    intd = 1
                    print(f"item{intd}       -> Inspect {x}")
                if "trapdoor" in inventoryitem1["unlocks"]:
                    print(
                        "keypad      -> Inspect KeyPad\n\n    --------------------------\n"
                    )
                else:
                    print(
                        "trapdoor    -> Inspect TrapDoor\n\n    --------------------------\n"
                    )
                if (
                    "Key Half 2 (Room 3)" in inventoryitem1["items"]
                    and "Key Half 1 (Room 3)" in inventoryitem1["items"]
                ):
                    print(
                        "craftkey   -> Combined key halfs\n\n    --------------------------\n"
                    )
                if escapeDoorLocation == "room2":
                    print("lockeddoor   -> Door")
                print(
                    "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
                )
                print("\n-----------------------------------------\n")
        elif UserInput.lower() == "item1":

            with open(jsonInventory, "r") as e:
                inventoryitem1 = json.load(e)
            print(dialog["clear"])
            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
            if inventoryitem1["locations"]["keylocation"] == "item1room2":
                if "item1room2" in inventoryitem1["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["pickupkey"]).format("Key Half 2 (Room 3)")
                    )
                    inventoryitem1["items"].append("Key Half 2 (Room 3)")
                    inventoryitem1["unlocks"].append("item1room2")
            else:
                if "item1room2" in inventoryitem1["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n - There is nothing here its just a {}",
                                "\n - Maybe there is nothing to this {}, its just bare.",
                            ]
                        ).format(currentItems[0])
                    )
                    inventoryitem1["unlocks"].append("item1room2")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem1, f, indent=2)

        elif UserInput.lower() == "item2":

            # currentItems[1]
            with open(jsonInventory, "r") as e:
                inventoryitem2 = json.load(e)
            print(dialog["clear"])
            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
            if inventoryitem2["locations"]["keylocation"] == "item2room2":
                if "item2room2" in inventoryitem2["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(dialog["clear"])
                    print(
                        random.choice(dialog["pickupkey"]).format("Key Half 2 (Room 3)")
                    )
                    inventoryitem2["items"].append("Key Half 2 (Room 3)")
                    inventoryitem2["unlocks"].append("item2room2")
            else:
                if "item2room2" in inventoryitem2["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n - There is nothing here its just a {}",
                                "\n - Maybe there is nothing to this {}, its just bare.",
                            ]
                        ).format(currentItems[1])
                    )
                    inventoryitem2["unlocks"].append("item2room2")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem2, f, indent=2)

        elif UserInput.lower() == "item3":
            # currentItems[2]

            with open(jsonInventory, "r") as e:
                inventoryitem3 = json.load(e)
            print(dialog["clear"])
            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
            if inventoryitem3["locations"]["keylocation"] == "item3room2":
                if "item3room2" in inventoryitem3["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["pickupkey"]).format("Key Half 2 (Room 3)")
                    )
                    inventoryitem3["items"].append("Key Half 2 (Room 3)")
                    inventoryitem3["unlocks"].append("item2room2")
            else:
                if "item2room2" in inventoryitem3["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n - There is nothing here its just a {}",
                                "\n - Maybe there is nothing to this {}, its just bare.",
                            ]
                        ).format(currentItems[2])
                    )
                    inventoryitem3["unlocks"].append("item2room2")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem3, f, indent=2)

        elif UserInput.lower() == "item4":
            # currentItems[3]

            with open(jsonInventory, "r") as e:
                inventoryitem4 = json.load(e)
            print(dialog["clear"])
            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
            if inventoryitem4["locations"]["keylocation"] == "item4room2":
                if "item4room2" in inventoryitem4["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["pickupkey"]).format("Key Half 2 (Room 3)")
                    )
                    inventoryitem4["items"].append("Key Half 2 (Room 3)")
                    inventoryitem4["unlocks"].append("item2room2")
            else:
                if "item2room2" in inventoryitem4["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n - There is nothing here its just a {}",
                                "\n - Maybe there is nothing to this {}, its just bare.",
                            ]
                        ).format(currentItems[3])
                    )
                    inventoryitem4["unlocks"].append("item2room2")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem4, f, indent=2)

        elif UserInput.lower() == "trapdoor":
            with open(jsonInventory, "r") as e:
                inventoryitem5 = json.load(e)
            if "trapdoor" in inventoryitem5["unlocks"]:
                print(dialog["clear"])
                print(dialog["commandError"])
            else:
                if "Black Light" in inventoryitem5["items"]:
                    print(dialog["clear"])
                    print(
                        random.choice(
                            [
                                "You lift the drop door theres a keypad, you use the blacklight on the keys, and see finger print on the keys {} {} {} {}",
                                "Its a trapdoor! * You pull a 10000 iq play * il use the blacklight to see finger prints, you shine the light on the keypad and see the finger prints on the keys {} {} {} {}",
                            ]
                        ).format(
                            inventoryitem5["otherdata"]["room2"][0],
                            inventoryitem5["otherdata"]["room2"][1],
                            inventoryitem5["otherdata"]["room2"][2],
                            inventoryitem5["otherdata"]["room2"][3],
                        )
                    )
                    inventoryitem5["unlocks"].append("trapdoor")
            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem5, f, indent=2)

        elif UserInput.lower() == "keypad":
            if "trapdoor" in inventoryitem5["unlocks"]:
                if "keypad" in inventoryitem5["unlocks"]:
                    print(dialog["clear"])
                    print(
                        random.choice(
                            [
                                "\nIv already looked in here, iv taken the key",
                                "\nmaybe this is a waste of time iv already looked in here!",
                            ]
                        )
                    )
                else:
                    while True:
                        print(dialog["clear"])
                        userinput = input(
                            f"Keypad: 4 digit       |  Known Numbers: {inventoryitem5['otherdata']['room2'][0]} {inventoryitem5['otherdata']['room2'][1]} {inventoryitem5['otherdata']['room2'][2]} {inventoryitem5['otherdata']['room2'][3]} \n>#> "
                        )
                        if not userinput.isnumeric():
                            print(dialog["clear"])
                            print(
                                random.choice(
                                    [
                                        "\nWait there are no letters on here",
                                        "\nMaybe its only numbers there are no letters on here",
                                    ]
                                )
                            )
                        elif str(userinput) == inventoryitem5["code"]["room2cabnet"]:
                            print(dialog["clear"])
                            print(
                                random.choice(
                                    [
                                        "\nbeep, beep, beep, Wait that worked? theres a key inside, wait no its broken maybe the other half is around here.",
                                        "\n* the box cracks open* oh how, wait NO! its broken maybe the other half is around here somewhere",
                                    ]
                                )
                            )
                            inventoryitem5["items"].append("Key Half 1 (Room 3)")
                            inventoryitem5["unlocks"].append("keypad")
                            break

                        else:
                            print(dialog["clear"])
                            print(
                                random.choice(
                                    [
                                        "\nThe number entered was incorrect.",
                                        "\nAunauthroized Access Code",
                                        "\nDamn it's the wrong code.",
                                        "\nSeriously?",
                                        "\nThis is a joke.",
                                        "\nGod damn it! We are almost out!",
                                        "\nHow many times will I get this wrong?",
                                        "\nCome on! Hurry it up!",
                                    ]
                                )
                            )
            else:
                print(dialog["clear"])
                print(dialog["commandError"])

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem5, f, indent=2)

        elif UserInput.lower() == "inventory":
            with open(jsonInventory, "r") as e:
                inventoryshow = json.load(e)
                print(dialog["clear"])
                print("\n-----------------------------------------\n")
                for x in inventoryshow["items"]:
                    print(x)
                print("\n-----------------------------------------\n")
        elif UserInput.lower() == "exit":
            print(dialog["clear"])
            return
        elif UserInput.lower() == "craftkey":
            with open(jsonInventory, "r") as e:
                inventorycraftkey = json.load(e)
            if (
                "Key Half 2 (Room 3)" in inventorycraftkey["items"]
                and "Key Half 1 (Room 3)" in inventorycraftkey["items"]
            ):
                print(dialog["clear"])
                print(
                    "\nBoth the keys fit together, how nice",
                    "\nmaybe this goes.. oh why was i worried they go together",
                    "\nMaybe this goes with this",
                )
                print("\n- You combined the keys and make a full key")
                with open(jsonInventory, "r") as e:
                    inventorycraftkey = json.load(e)
                inventorycraftkey["items"].remove("Key Half 2 (Room 3)")
                inventorycraftkey["items"].remove("Key Half 1 (Room 3)")
                inventorycraftkey["items"].append("Key (Room 3)")
                with open(jsonInventory, "w") as f:
                    json.dump(inventorycraftkey, f, indent=2)
            else:
                print(dialog["clear"])
                print(dialog["commandError"])
        elif UserInput.lower() == "lockeddoor":
            if escapeDoorLocation == "room2":
                with open(jsonInventory, "r") as e:
                    inventoryshow = json.load(e)
                if "Key (Exit)" in inventoryshow["items"]:
                    timestamp = int(time.time()) - inventoryshow["timestart"]
                    dt_object = f"{round(timestamp / 60, 2)} Minutes"
                    currenttime = time.ctime(time.time())
                    print(dialog["clear"])
                    print(
                        dialog["escapewin"].format(
                            scene,
                            sideCharacter,
                            antagonistCharacter,
                            currenttime,
                            dt_object,
                        )
                    )
                    time.sleep(3)
                    print(dialog["info"])
                    sys.exit()
                else:
                    print(dialog["clear"])
                    print(
                        random.choice(
                            [
                                "\nIts locked!, maybe i could find a key somewhere",
                                "\nIts locked, I need a key",
                                "\nIts locked, maybe i can kick the door down\n*You try to kick the door down*\nIt wont budge, Maybe i have to find a key for it.",
                            ]
                        )
                    )
            else:
                print(dialog["clear"])
                print(dialog["commandError"])
        else:
            print(dialog["clear"])
            print(dialog["commandError"])
