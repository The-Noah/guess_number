import random

number = random.randint(1, 10)
won = False
turns = 0

while won == False:
  try:
    guess = int(input("Enter a number between 1 and 10: "))
  except KeyboardInterrupt:
    print()
    print("Bye :(")
    break
  except:
    print("Invalid input")
    continue

  turns += 1

  if guess < 1 or guess > 10:
    print("Your guess must be between 1 and 10")
    continue
  
  if number == guess:
    print("You won!")
    print("Number of turns it took: ", turns)
    won == True
    break
  else:
    if number > guess:
      print("Your guess was low")
    else:
      print("Your guess was high")
