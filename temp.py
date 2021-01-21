
decrypt = ""
decodelist = []

inventoryitem5 = "9 5 7 5 7"

for x in inventoryitem5.split(" "):
  if x == "0":
    decodelist.append("7")
  if x == "1":
    decodelist.append("2")
  if x == "2":
    decodelist.append("6")
  if x == "3":
    decodelist.append("0")
  if x == "4":
    decodelist.append("3")
  if x == "5":
    decodelist.append("4")
  if x == "6":
    decodelist.append("1")
  if x == "7":
    decodelist.append("8")
  if x == "8":
    decodelist.append("9")
  if x == "9":
    decodelist.append("5")
    

print("".join(decodelist))