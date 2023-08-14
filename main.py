# Dhrumit Savaliya and Smit Lila
# A program that simulates an escape room by having the user open a series of three doors
# random chosen from several different types of doors. Use the following class diagram to create the program
#
# Dhrumit - I did main.py / BasicDoor.py / CodeDoor.py / door.py
# Smit - I did LockedDoor.py / DeadboltDoor.py / ComboDoor.py / 


import random
from door import Door
from BasicDoor import BasicDoor
from CodeDoor import CodeDoor
from ComboDoor import ComboDoor
from DeadboltDoor import DeadboltDoor
from LockedDoor import LockedDoor

def open_door(door: Door) -> bool:
  '''Printing the description of the door using the 'examine_door' method of the 'Door' class.'''
  print(door.examine_door())
  while not door.is_unlocked(): #Creating a loop that continues until the door is unlocked using the 'is_unlocked' method of the 'Door' class.
    print(door.menu_options()) #Printing the menu options for attempting to unlock the door using the 'menu_options' method of the 'Door' class.
    try: #Using a 'try-except' block to catch any invalid input that is not an integer.
      option = int(input("\nEnter an option: "))
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
      continue
    result = door.attempt(option) #Attempting to unlock the door using the 'attempt' method of the 'Door' class and printing the result.
    print(result)
    if not door.is_unlocked(): #If the door is not unlocked, prompting the user to search somewhere else using the 'clue' method of the 'Door' class.
      print(door.clue())
  print(door.success())#Printing a success message using the 'success' method of the 'Door' class.
  return True #Returning True if the door was successfully opened.


def main():
  '''Defining a function 'main' that initializes the game by printing a welcome message and explaining the objective.'''
  print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...\n")

  doors = [BasicDoor(), LockedDoor(), DeadboltDoor(), ComboDoor(), CodeDoor()]

  for i in range(3):
    '''Looping through the list of doors three times, selecting a random door from the list using the 'random.choice' method, and attempting to open it using the 'open_door' function. Removing the opened door from the list.'''
    door = random.choice(doors)
    open_door(door)
    doors.remove(door)

  print("\nCongratulations! You escaped...this time.")


if __name__ == '__main__':
  main()
