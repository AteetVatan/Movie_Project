"""Module for Main screen Print strings."""
from enum import Enum
from helpers.base_print import BasePrint


class MainPrintEnum(Enum):
    """Enumeration to define Print strings keys."""
    WELCOME = 1
    ENTER_CHOICE = 2
    CONTINUE = 3
    INVALID = 4
    MENU = 5


class MainPrint(BasePrint):
    """Class containing Print strings."""
    _prompt_dictionary = {MainPrintEnum.WELCOME.value: '********** My Movies Database **********',
                          MainPrintEnum.ENTER_CHOICE.value: 'Enter choice (1-{key1}): ',
                          MainPrintEnum.CONTINUE.value: 'Press enter to continue',
                          MainPrintEnum.INVALID.value: 'Invalid Choice',
                          MainPrintEnum.MENU.value: 'Menu:'}
