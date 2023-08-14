import random
from door import Door


class BasicDoor(Door):

  def __init__(self):
    '''The constructor method for the BasicDoor class that initializes the door's state and status.'''
    self._state = bool(random.getrandbits(1))  # Set the state of the door to a random boolean value.
    self._status = False # Set the status of the door to False.

  def examine_door(self) -> str:
    '''A method that returns a string describing the door.'''
    return "You encounter a basic door, you can either push it or pull it to open."

  def menu_options(self) -> str:
    '''A method that returns the available menu options for the door.'''
    return "1. Push.\n2. Pull."

  def get_menu_max(self) -> int:
    '''A method that returns the maximum number of menu options available for the door.'''
    return 2

  def attempt(self, option: int) -> str:
    '''A method that attempts to open the door based on the selected menu option.'''
    if option == 1 and not self._state or option == 2 and self._state: # If the selected option matches the state of the door, set the status of the door to True and return a success message.
      self._status = True
      return "The door opens!"
    else: # If the selected option does not match the state of the door, return a failure message.
      return "The door doesn't opens."

  def is_unlocked(self) -> bool:
    return self._status

  def clue(self) -> str:
    '''A method that returns a clue to help the player open the door.'''
    return 'Try the other way.'

  def success(self) -> str:
    '''A method that returns a success message when the door is successfully opened.'''
    return "You have successfully opened the door!\n"





            
        
