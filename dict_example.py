a = {
  "name" : "Jerrick",
  "money" : 20000000000000000000000
}

print (a)
print (type(a))
print (len(a))
a["age"] = 13
print (a)
print (a["name"])
print (a["money"])
print (a.keys())
print (a.values())

a["money"] = 0
print (a)

del a['age']
print(a)