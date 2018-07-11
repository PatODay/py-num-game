from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
	print "Please choose a number between 2 and %d" % max_val
  else:
    print "Rolling..."
    sleep(2)
    print "%d on the first roll" % first_roll
    sleep(1)
    print "%d on the second roll" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You've won!"
    else:
      print "Sorry, you lost"

roll_dice(6)
