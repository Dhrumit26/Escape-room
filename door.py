from abc import ABC, abstractmethod
'''Import the ABC (Abstract Base Class) and abstractmethod from the abc module'''

class Door(ABC):
    '''Define abstract methods for examining the door, returning menu options, 
    getting the maximum menu value, attempting to unlock the door, checking if 
    the door is unlocked, giving a clue to the user, and returning a success message 
    for unlocking the door'''
    @abstractmethod
    def examine_door(self) -> str:
        pass

    @abstractmethod
    def menu_options(self) -> str:
        pass

    @abstractmethod
    def get_menu_max(self) -> int:
        pass

    @abstractmethod
    def attempt(self, option: int) -> str:
        pass

    @abstractmethod
    def is_unlocked(self) -> bool:
        pass

    @abstractmethod
    def clue(self) -> str:
        pass

    @abstractmethod
    def success(self) -> str:
        pass
