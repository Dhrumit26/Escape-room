import random
from door import Door


class CodeDoor(Door):

  def __init__(self):
    '''Constructor that initializes the correct code with a list of three random 'X' or 'O' values'''
    self._correct_code = [random.choice(['X', 'O']) for _ in range(3)]

  def examine_door(self):
    '''Method to return a message for examining the door'''
    return "A door with a coded keypad with three characters. Each key toggles a value with an 'X' or 'O'."

  def menu_options(self):
    '''Method to return the menu options'''
    return "1. Press Key 1.\n2. Press Key 2.\n3. Press Key 3."

  def get_menu_max(self):
    '''Method to return the maximum menu value'''
    return 3

  def attempt(self, option):
    '''Method to attempt to unlock the door by toggling the value of the key'''
    self._correct_code[option - 1] = 'X' if self._correct_code[option - 1] == 'O' else 'O'
    return f"You pressed key {option}"

  def is_unlocked(self):
    '''Method to check if the door is unlocked'''
    return self._correct_code == ['X', 'X', 'O']

  def clue(self):
    '''Method to give a clue to the user for unlocking the door'''
    count_correct = sum(c1 == c2 for c1, c2 in zip(self._correct_code, ['X', 'X', 'O']))
    return f"The Right Code is {self._correct_code}. The number of correct characters is {count_correct}"

  def success(self) -> str:
    '''Method to return success message for unlocking the door'''
    return "You successfully unlocked the deadbolt door.\n"





    