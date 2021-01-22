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
  dialogJson = json.load(a)
with open(jsonFileRoom, 'r') as b:
  roomjson = json.load(b)
with open(jsonFileBase, 'r') as c:
  baseData = json.load(c)
with open(jsonFileData, 'r') as d:
  data = json.load(d)
with open(jsonInventory, 'r') as e:
  inventory = json.load(e)

def cal():
  items = 0
  dialog = 0
  rooms = 0
  other = 0
  linesOfCode = 0

  for x in itemJson:
    for i in x:
      items += 1

  for x in dialogJson:
    try:
      for i in x:
        dialog += 1
    except:
      dialog += 1

  for x in roomjson:
    for i in x:
      rooms += 1

  for x in baseData:
    try:
      for i in x:
        other += 1
    except:
      other += 1

  with open("main.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1

  with open("Rooms/Room1.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1

  with open("Rooms/Room2.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("Rooms/Room3.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("Rooms/Room4.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("Rooms/Room5.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
  
  with open("jsonFiles/BaseData.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
  
  with open("jsonFiles/data.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("jsonFiles/dialog.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("jsonFiles/inventory.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("jsonFiles/items.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("jsonFiles/randomRoom.json", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1
    
  with open("calculate.py", 'r') as d:
    for x in d.readlines():
      linesOfCode += 1

  x = {     
    "allvar": items + dialog + rooms + other,
    "allposs": items * rooms * other,
    "lines": linesOfCode,
    "perc": str((items + dialog + rooms + other) / (items * rooms * other * dialog) * 100)[:4]
  }    

  return x