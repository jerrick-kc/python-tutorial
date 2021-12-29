coins = int(input("How many coins do you have?"))
if (coins == 0):
  print ("You are poor please leave!")
if (coins >= 1000):
  print ("Wow you are rich!!!")
elif (coins <= 30):
  print ("You can buy this :)")
else:
  print ("You cannot buy this")

print ("Bye Bye")