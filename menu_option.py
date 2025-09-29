from enum import Enum, auto
from project_exceptions import OptionException

class Option(Enum):
    SAVE_NEW_ENTRY = auto() # or use integer value
    SEARCH_BY_ID = auto()
    PRINT_AGE_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    TRY_EXIT = auto()
    SAVE_ALL_DATA = auto()
    INVALID_OPTION = auto()

def printError(option):
    print("Error: Option [" + option + "] does not exist. Please try again")

def convertInputToOption(option):
    if option.isdigit() == False:
        raise OptionException(option)
    
    option = int(option)
    
    if option == 1:
        return Option.SAVE_NEW_ENTRY
    elif option == 2:
        return Option.SEARCH_BY_ID
    if option == 3:
        return Option.PRINT_AGE_AVERAGE
    elif option == 4:
        return Option.PRINT_ALL_NAMES
    if option == 5:
        return Option.PRINT_ALL_IDS
    elif option == 6:
        return Option.PRINT_ALL_ENTRIES
    if option == 7:
        return Option.PRINT_ENTRY_BY_INDEX
    elif option == 8:
        return Option.SAVE_ALL_DATA
    elif option == 9:
        return Option.TRY_EXIT
    else:
        raise OptionException(option)