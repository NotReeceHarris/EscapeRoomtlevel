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


def Room5Start(
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
    print(dialog["clear"])
    print(f"\n{random.choice(dialog[f'{scene}{roomName5}'])}")
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
            with open(jsonInventory, "r") as e:
                inventoryreset = json.load(e)
            inventoryreset["locations"]["keylocation"] = x
            inventoryreset["locations"]["otherlocation"] = y
            with open(jsonInventory, "w") as f:
                json.dump(inventoryreset, f, indent=2)
            break

    while True:

        if specialRoom == roomName1:
            specialRoom = True
        UserInput = input(
            str(commandLine.format(roomName5))
        )  # The input is put in the varaible UserInput

        if UserInput.lower() == "help":
            print(dialog["clear"])
            print("\n-----------------------------------------\n")
            intd = 0
            for x in currentItems:
                intd = 1
                print(f"item{intd}       -> Inspect {x}")
            print("vault       -> Inspect Vault\n\n    --------------------------\n")
            if escapeDoorLocation == "room5":
                print("lockeddoor   -> Door")
            print(
                "help         -> Help Menu\ninventory    -> Opens your inventory\nexit         -> Return to corridor"
            )
            print("\n-----------------------------------------\n")
        elif UserInput.lower() == "item1":
            print(dialog["clear"])
            with open(jsonInventory, "r") as e:
                inventoryitem1 = json.load(e)

            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[0]))
            if inventoryitem1["locations"]["keylocation"] == "item1room5":
                if "item1room5" in inventoryitem1["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["decryptiongraph"]).format(
                            "Decrypt table part 5"
                        )
                    )
                    inventoryitem1["items"].append("Decrypt table part 5")
                    inventoryitem1["unlocks"].append("item1room5")
            elif inventoryitem1["locations"]["otherlocation"] == "item1room5":
                if "item1room5" in inventoryitem1["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n- A peice of paper? its all wet, but i can only just see a passcode {}",
                                "\n - Paper? maybe it has someth... a number {} i should remember this.",
                            ]
                        ).format("Decrypt table part 6")
                    )
                    inventoryitem1["items"].append("Decrypt table part 6")
                    inventoryitem1["unlocks"].append("item1room5")
                    inventoryitem1["unlocks"].append("room5paper")
            else:
                if "item1room5" in inventoryitem1["unlocks"]:
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
                    inventoryitem1["unlocks"].append("item1room5")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem1, f, indent=2)

        elif UserInput.lower() == "item2":
            print(dialog["clear"])
            # currentItems[1]
            with open(jsonInventory, "r") as e:
                inventoryitem2 = json.load(e)

            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[1]))
            if inventoryitem2["locations"]["keylocation"] == "item2room5":
                if "item2room5" in inventoryitem2["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["decryptiongraph"]).format(
                            "Decrypt table part 5"
                        )
                    )
                    inventoryitem2["items"].append("Decrypt table part 5")
                    inventoryitem2["unlocks"].append("item2room5")
            elif inventoryitem2["locations"]["otherlocation"] == "item2room5":
                if "item2room5" in inventoryitem2["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n- A peice of paper? its all wet, but i can only just see a passcode {}",
                                "\n - Paper? maybe it has someth... a number {} i should remember this.",
                            ]
                        ).format("Decrypt table part 6")
                    )
                    inventoryitem2["items"].append("Decrypt table part 6")
                    inventoryitem2["unlocks"].append("item2room5")
                    inventoryitem2["unlocks"].append("room5paper")
            else:
                if "item2room5" in inventoryitem2["unlocks"]:
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
                    inventoryitem2["unlocks"].append("item2room5")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem2, f, indent=2)

        elif UserInput.lower() == "item3":
            print(dialog["clear"])
            # currentItems[2]

            with open(jsonInventory, "r") as e:
                inventoryitem3 = json.load(e)

            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[2]))
            if inventoryitem3["locations"]["keylocation"] == "item3room5":
                if "item3room5" in inventoryitem3["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(dialog["decryptiongraph"]).format(
                            "Decrypt table part 5"
                        )
                    )
                    inventoryitem3["items"].append("Decrypt table part 5")
                    inventoryitem3["unlocks"].append("item3room5")
            elif inventoryitem3["locations"]["otherlocation"] == "item3room5":
                if "item3room5" in inventoryitem3["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n- A peice of paper? its all wet, but i can only just see a passcode {}",
                                "\n - Paper? maybe it has someth... a number {} i should remember this.",
                            ]
                        ).format("Decrypt table part 6")
                    )
                    inventoryitem3["items"].append("Decrypt table part 6")
                    inventoryitem3["unlocks"].append("item3room5")
                    inventoryitem3["unlocks"].append("room5paper")
            else:
                if "item3room5" in inventoryitem3["unlocks"]:
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
                    inventoryitem3["unlocks"].append("item3room5")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem3, f, indent=2)

        elif UserInput.lower() == "item4":
            # currentItems[3]
            print(dialog["clear"])

            with open(jsonInventory, "r") as e:
                inventoryitem4 = json.load(e)

            print(random.choice(dialog["iteminspectdialog"]).format(currentItems[3]))
            if inventoryitem4["locations"]["keylocation"] == "item4room5":
                if "item4room5" in inventoryitem4["unlocks"]:
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(dialog["clear"])
                    print(
                        random.choice(dialog["decryptiongraph"]).format(
                            "Decrypt table part 5"
                        )
                    )
                    inventoryitem4["items"].append("Decrypt table part 5")
                    inventoryitem4["unlocks"].append("item4room5")
            elif inventoryitem4["locations"]["otherlocation"] == "item4room5":
                if "item4room5" in inventoryitem4["unlocks"]:
                    print(dialog["clear"])
                    print(random.choice(dialog["alreadysearched"]))
                else:
                    print(
                        random.choice(
                            [
                                "\n- A peice of paper? its all wet, but i can only just see a passcode {}",
                                "\n - Paper? maybe it has someth... a number {} i should remember this.",
                            ]
                        ).format("Decrypt table part 6")
                    )
                    inventoryitem4["items"].append("Decrypt table part 6")
                    inventoryitem4["unlocks"].append("item4room5")
                    inventoryitem4["unlocks"].append("room5paper")
            else:
                if "item4room5" in inventoryitem4["unlocks"]:
                    print(dialog["clear"])
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
                    inventoryitem4["unlocks"].append("item4room5")

            with open(jsonInventory, "w") as f:
                json.dump(inventoryitem4, f, indent=2)

        elif UserInput.lower() == "vault":
            print(dialog["clear"])
            with open(jsonInventory, "r") as e:
                inventoryitem5 = json.load(e)

            decrypt = ""

            if difficulty == 1:
              for x in inventoryitem5["code"]["dif1num"].split(" "):
                if x == "0":
                  decrypt = decrypt + "7"
                if x == "1":
                  decrypt = decrypt + "2"
                if x == "2":
                  decrypt = decrypt + "6"
                if x == "3":
                  decrypt = decrypt + "0"
                if x == "4":
                  decrypt = decrypt + "3"
                if x == "5":
                  decrypt = decrypt + "4"
                if x == "6":
                  decrypt = decrypt + "1"
                if x == "7":
                  decrypt = decrypt + "8"
                if x == "8":
                  decrypt = decrypt + "9"
                if x == "9":
                  decrypt = decrypt + "5"
            elif difficulty == 2:
              for x in inventoryitem5["code"]["dif2num"].split(" "):
                if x == "0":
                  decrypt = decrypt + "7"
                if x == "1":
                  decrypt = decrypt + "2"
                if x == "2":
                  decrypt = decrypt + "6"
                if x == "3":
                  decrypt = decrypt + "0"
                if x == "4":
                  decrypt = decrypt + "3"
                if x == "5":
                  decrypt = decrypt + "4"
                if x == "6":
                  decrypt = decrypt + "1"
                if x == "7":
                  decrypt = decrypt + "8"
                if x == "8":
                  decrypt = decrypt + "9"
                if x == "9":
                  decrypt = decrypt + "5"
            elif difficulty == 3:
              for x in inventoryitem5["code"]["dif3num"].split(" "):
                if x == "0":
                  decrypt = decrypt + "7"
                if x == "1":
                  decrypt = decrypt + "2"
                if x == "2":
                  decrypt = decrypt + "6"
                if x == "3":
                  decrypt = decrypt + "0"
                if x == "4":
                  decrypt = decrypt + "3"
                if x == "5":
                  decrypt = decrypt + "4"
                if x == "6":
                  decrypt = decrypt + "1"
                if x == "7":
                  decrypt = decrypt + "8"
                if x == "8":
                  decrypt = decrypt + "9"
                if x == "9":
                  decrypt = decrypt + "5"

            if (
                "Decrypt table part 1" in inventoryitem5["otherdata"]["table"]
                and "Decrypt table part 2" in inventoryitem5["otherdata"]["table"]
                and "Decrypt table part 3" in inventoryitem5["otherdata"]["table"]
                and "Decrypt table part 4" in inventoryitem5["otherdata"]["table"]
                and "Decrypt table part 5" in inventoryitem5["otherdata"]["table"]
                and "Decrypt table part 6" in inventoryitem5["otherdata"]["table"]
            ):
                if "vaultopen" in inventoryitem5["unlocks"]:
                    print(dialog["clear"])
                    print(
                        random.choice(
                            [
                                "\nNO! IM NOT DOING THIS AGAIN IM GOING\n",
                                "\nTHERES NO TIME LETS GET OUT OF HERE\n",
                                " \nI HAVE THE KEY LETS GET OUT\n",
                            ]
                        )
                    )
                elif "vault" in inventoryitem5["unlocks"]:
                    with open(jsonInventory, "r") as e:
                        inventoryvault = json.load(e)
                    inventoryvault["unlocks"].append("vault")
                    with open(jsonInventory, "w") as f:
                        json.dump(inventoryvault, f, indent=2)
                    while True:
                        if difficulty == 1:
                            userinput = input(
                                f"Vault Lock |   Etched Number : {inventoryitem5['code']['dif1num']}\n>#>"
                            )
                            if str(userinput) == str(decrypt):
                                print(dialog["clear"])
                                print(
                                    f"Omg it worked it opend wait there is only 2 items why is there ONLY 2 items inside a huge vault, wait what is it a Key it says 'Exit' on it and a {specialItem} well lets go find {sideCharacter} and escape!"
                                )
                                with open(jsonInventory, "r") as e:
                                    inventoryvault = json.load(e)

                                inventoryvault["unlocks"].append("vaultopen")
                                inventoryvault["items"].append("Key (Exit)")
                                inventoryvault["items"].append(f"{specialItem}")
                                inventoryvault["unlocks"].append("sidedeath")

                                with open(jsonInventory, "w") as f:
                                    json.dump(inventoryvault, f, indent=2)
                            else:
                                print(dialog["clear"])
                                print(
                                    random.choice(
                                        [
                                            "\nThe number entered was incorrect.",
                                            "\nAccess Denied.",
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
                            break

                        elif difficulty == 2:
                            userinput = input(
                                f"Vault Lock |   Etched Number : {inventoryitem5['code']['dif2num']}\n>#>"
                            )
                            if str(userinput) == str(decrypt):
                                print(dialog["clear"])
                                print(
                                    f"Omg it worked it opend wait there is only 2 items why is there ONLY 2 items inside a huge vault, wait what is it a Key it says 'Exit' on it and a {specialItem} well lets go find {sideCharacter} and escape!"
                                )
                                with open(jsonInventory, "r") as e:
                                    inventoryitem5 = json.load(e)
                                with open(jsonInventory, "r") as e:
                                    inventoryvault = json.load(e)

                                inventoryvault["unlocks"].append("vaultopen")
                                inventoryvault["items"].append("Key (Exit)")
                                inventoryvault["items"].append(f"{specialItem}")
                                inventoryvault["unlocks"].append("sidedeath")

                                with open(jsonInventory, "w") as f:
                                    json.dump(inventoryvault, f, indent=2)
                            else:
                                print(dialog["clear"])
                                print(
                                    random.choice(
                                        [
                                            "\nThe number entered was incorrect.",
                                            "\nAccess Denied.",
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
                            break

                        elif difficulty == 3:
                            userinput = input(
                                f"Vault Lock |   Etched Number : {inventoryitem5['code']['dif3num']}\n>#>"
                            )
                            if str(userinput) == str(decrypt):
                                print(dialog["clear"])
                                print(
                                    f"Omg it worked it opend wait there is only 2 items why is there ONLY 2 items inside a huge vault, wait what is it a Key it says 'Exit' on it and a {specialItem} well lets go find {sideCharacter} and escape!"
                                )
                                with open(jsonInventory, "r") as e:
                                    inventoryvault = json.load(e)

                                inventoryvault["unlocks"].append("vaultopen")
                                inventoryvault["items"].append("Key (Exit)")
                                inventoryvault["items"].append(f"{specialItem}")
                                inventoryvault["unlocks"].append("sidedeath")

                                with open(jsonInventory, "w") as f:
                                    json.dump(inventoryvault, f, indent=2)
                            else:
                                print(dialog["clear"])
                                print(
                                    random.choice(
                                        [
                                            "\nThe number entered was incorrect.",
                                            "\nAccess Denied.",
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
                            break

                            if not userinput.isnumeric():
                                print(dialog["clear"])
                                print(
                                    random.choice(
                                        [
                                            "\nThis keypad only has numbers, not letters.",
                                            "\nHuh? I dont see a letter here",
                                            "\nMaybe its a number there are no numbers here",
                                        ]
                                    )
                                )

                else:
                    with open(jsonInventory, "r") as e:
                        inventoryshow = json.load(e)

                    if difficulty == 1:
                        print(dialog["clear"])
                        print(
                            random.choice(
                                [
                                    "\nThe vault looks like it has stuff etched into it it says {}, maybe this is the code huh simple\n",
                                    "Is that a number? wait no its etched into the vault huh it says.. {}",
                                ]
                            ).format(inventoryshow["code"]["dif1num"])
                        )
                        inventoryshow["unlocks"].append("vault")
                    elif difficulty == 2:
                        print(dialog["clear"])
                        print(
                            random.choice(
                                [
                                    "\nThe vault looks like it has stuff etched into it it says {}, maybe this is the code huh simple\n",
                                    "Is that a number? wait no its etched into the vault huh it says.. {}",
                                ]
                            ).format(inventoryshow["code"]["dif2num"])
                        )
                        inventoryshow["unlocks"].append("vault")
                    elif difficulty == 3:
                        print(dialog["clear"])
                        print(
                            random.choice(
                                [
                                    "\nThe vault looks like it has stuff etched into it it says {}, maybe this is the code huh simple\n",
                                    "Is that a number? wait no its etched into the vault huh it says.. {}",
                                ]
                            ).format(inventoryshow["code"]["dif3num"])
                        )
                        inventoryshow["unlocks"].append("vault")
                    else:
                        print(f"test {difficulty}")
                    with open(jsonInventory, "w") as f:
                        json.dump(inventoryshow, f, indent=2)

            else:
                print(dialog["clear"])
                print(
                    random.choice(
                        [
                            "Maybe i should go put my peices of the decode gragh on the table",
                            "iv still got some decode peices maybe i should go check the table",
                        ]
                    )
                )

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
        elif UserInput.lower() == "lockeddoor":
            if escapeDoorLocation == "room5":
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