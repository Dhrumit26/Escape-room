import random
from door import Door


class DeadboltDoor(Door):

  def __init__(self):
    '''The init method initializes the DeadboltDoor object with two random bolts that are either locked or unlocked.'''
    self._bolt_1 = bool(random.getrandbits(1))
    self._bolt_2 = not self._bolt_1  

  def examine_door(self):
    '''The examine_door method returns a string that describes the door.'''
    return "You encountered a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked."

  def menu_options(self):
    '''The menu_options method returns a string with the available options for unlocking the door.'''
    return "1. Toggle Bolt 1.\n2. Toggle Bolt 2."

  def get_menu_max(self):
    '''The get_menu_max method returns the maximum number of menu options.'''
    return 2

  def attempt(self, option):
    '''The attempt method takes an option as input and toggles the corresponding bolt accordingly, returning a message to the user.'''
    if option == 1:
      self._bolt_1 = not self._bolt_1
      return "You toggle the first bolt."
    elif option == 2:
      self._bolt_2 = not self._bolt_2
      return "You toggle the second bolt."
    else:
      return "Invalid option."

  def is_unlocked(self):
    '''The is_unlocked method checks if both bolts are unlocked and returns True if so.'''
    return self._bolt_1 == False and self._bolt_2 == False

  def clue(self):
    '''The clue method returns a message to the user giving a hint as to the status of the bolts.'''
    if self._bolt_1 == False or self._bolt_2 == False:
      return "You jiggle the door...it seems like one of the bolts is unlocked."
    else:
      return "You jiggle the door...it's completely locked."

  def success(self) -> str:
    '''The success method returns a message to the user indicating that both bolts have been unlocked and the door has been opened.'''
    return "You unlocked both deadbolts and opened the door.\n"
