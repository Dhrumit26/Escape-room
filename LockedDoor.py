import random
from door import Door


class LockedDoor(Door):

  def __init__(self):
    '''Initializing the class with three instance variables, '_key_location' which holds a random integer between 1 and 3, '_input' which is set to False, and '_status' which is set to False.'''
    self._key_location = random.randint(1, 3)
    self._input = False
    self._status = False

  def examine_door(self) -> str:
    '''Defining a method 'examine_door' that returns a string describing the door as locked and prompts the user to search for the key.'''
    return "A locked door. Look around for the key."

  def menu_options(self) -> str:
    '''Defining a method 'menu_options' that returns a string with three options for the user to attempt to find the key.'''
    return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."

  def get_menu_max(self) -> int:
    '''Defining a method 'get_menu_max' that returns the maximum number of menu options.'''
    return 3

  def attempt(self, option: int) -> str:
    '''Defining a method 'attempt' that takes an integer 'option' and checks if the door is already unlocked or if the input matches the random key location, and then unlocks the door and changes the status if the input matches the key location'''
    if not self._status and option == self._key_location:
      self._input = True
      self._status = True
      return "Congo! You unlock the door and it opens!"
    elif self._status:
      return "The door is already unlocked."
    else:
      return "You don't find anything."

  def is_unlocked(self) -> bool:

    return self._status

  def clue(self) -> str:

    return "Look somewhere else."

  def success(self) -> str:
    return "You have successfully opened the door!\n"



