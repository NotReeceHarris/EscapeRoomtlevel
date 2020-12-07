import json

with open("jsonFiles/data.json", 'r') as f:
        data = json.load(f)

InventorySpace = data["inventory"]
global InventoryLeft
InventoryLeft = 1
Inv = ["Key 1"]
BlackList = []


def SeeI():
    if Inv == []:
        print(
            '-------------------------------------\nYour Inventory is EMPTY\n-------------------------------------'
        )
    else:
        global InventoryLeft
        print('-------------------------------------')
        for x in Inv:
            print(f' |  {x}  | ({InventoryLeft} / {InventorySpace})')
            InventoryLeft += 1


def AddI(appendi):
    global InventoryLeft
    if InventoryLeft == 10:
        print('-------------------------------------')
        print("Your Inventory is full")
    else:
        Inv.append(appendi)
        print('-------------------------------------')
        print(f'{appendi} has been added to inventory')


def DropI(Item):
    global InventoryLeft
    if Item in BlackList:
        print('-------------------------------------')
        print(f'{Item}, Can not be dropped')
    else:
        if Item in Inv:
            InventoryLeft -= 1
            Inv.remove(Item)
            print('-------------------------------------')
            print(f'{Item}, Item has been dropped')
        else:
            print('-------------------------------------')
            print(f'You try to drop this item but fail (ERROR)')