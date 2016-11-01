#! /usr/bin/python
import random

guessesTaken = 0
getCoins = 0

print('Hello what is your name?')
myName = input()

def main():
  global guessesTaken 
  global getCoins
  # Asks which command you want to run.
  handleGuess  = random.randint(1, 10)
  word = input('To make a guess type "guess"\n To look at how many coins you have type "coins"\n To run a look to make guesses for you type "start"').strip().lower()
  # Runs the command/s.
  if word == "guess":
    while guessesTaken < 11:
      print('make guess')
      guess = input()
      guess = int(guess)

      guessesTaken = guessesTaken + 1
      
      if guess == handleGuess:
        getCoins = getCoins + 1
        handleGuess = random.randint(1, 10)
        print('gooood!')
      else:
        print('NOPE')

  elif word == "coins":
      print(myName, 'you have', getCoins)

  elif word == "start":
    while guessesTaken < 1000:
      startGuessing = random.randint(1, 10) 

      guessesTaken = guessesTaken + 1

      if startGuessing == handleGuess:
        getCoins = getCoins + 1
        handleGuess = random.randint(1, 10)
        print('you got a coin!')
      else:
        print('failed')
  elif word == "quit":
    return False
  else:
    print("Command not found")
  return True
while main():
  pass
