print("Hi! Today the computer will be trying to guess your secret number. Think of an integer between 1 and 100!")
print()
start = 1
end = 100
answer_not_found = True
#Here you define the starting and the ending points of the range in which the secret number is in. In addition you can create a boolean which can be used in a while command until the answer is found so the loop can break.

while (answer_not_found): #The game will run until answer_not_found becomes false
  avg = int((start + end) / 2) #By finding the average of start and end we can slowly widdle down the range
  print ('start:', start, ', end:', end, ', avg:', avg, ', answer_not_found:', answer_not_found) #Optional command useful for seeing what each value is after each command
  if (start + 1 == end):
    response = int(input('If your number is ' + str(start) + ' please enter 1 otherwise enter 2: '))
    if (response == 1):
      print('Your number was', start)
      answer_not_found = False
    else:
      print('Your number was', end)
      answer_not_found = False 
  else:
    num = int(input('If your number is less than or equal to ' + str(avg)  + ' please enter 1, if not enter 2: '))
    if (num == 1):
      end = avg
    else:
      start = avg + 1
print('END')