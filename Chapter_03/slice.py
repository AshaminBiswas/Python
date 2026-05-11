#slice string
name  = "Ashamin"
sliceName = name[0:4]
print(sliceName)


number = "0123456789"
newNum = number[1:10:2]#its return the value skip by two index
print(newNum)

print(len(number))
print(name.endswith("in"))
print(name.replace("Ashamin", "Biswas"))