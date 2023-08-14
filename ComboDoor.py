import random
from door import Door


class ComboDoor(Door):

  def __init__(self):
    '''Constructor that initializes the correct value of combination lock and input to None'''
    self._correct_value = random.randint(1, 10)
    self._input = None

  def examine_door(self):
    '''Method to return a message for examining the door'''
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    '''Method to return the menu options'''
    return "Enter a number (1-10)"

  def get_menu_max(self):
    '''Method to return the maximum menu value'''
    return 10

  def attempt(self, option):
    '''Method to attempt to open the door'''
    self._input = int(option)
    if self._input == self._correct_value:
      return f"You turn the dial to {option} and hear a satisfying click."
    else:
      return f"You turn the dial to {option}, but nothing happens."

  def is_unlocked(self):
    '''Method to check if the door is unlocked'''
    return self._input == self._correct_value

  def clue(self):
    '''Method to give a clue to the user for opening the door'''
    if self._correct_value > self._input:
      return "Too High."
    else:
      return "Too Low."

  def success(self):
    return "You found the correct number and opened the door.\n"





            
        
