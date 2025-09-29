import pandas as pd
from menu_option import Option, convertInputToOption
from project_exceptions import *
from utils import *
from input_validation import mustBeNumberCheck
#############################################################################################################################################################
# Main functions

def saveNewEntry(data_dict: dict, data_list: list, age_average: float) -> float:
    new_person = getProfile()
    if new_person == None:
        return age_average
    
    id = new_person.getID()
    age = new_person.getAge()
    
    num_entries = len(data_dict)
    data_list.append(new_person)
    
    data_dict[id] = new_person
    sum_of_ages = num_entries* age_average + age
    age_average = sum_of_ages / (num_entries + 1)
    print("ID [" + str(id) + "] saved successfully")
    return age_average

def searchById(data_dict: dict):
    id = input("Please enter the ID you want to look for: ")
    id = mustBeNumberCheck("ID", id)
    if id not in data_dict:
        print("Error: ID " + str(id) + " is not saved")
    else:
        person= data_dict[id]
        printEntry(person)  

def printAgesAverage(age_average: float):
    print(age_average)

def printAllNames(data_dict: dict):
    for index, person in enumerate(data_dict.values()):
        print(str(index) + ". " + person.getName())

def printAllIds(data_dict: dict):
    for index, id in enumerate(data_dict):
        print(str(index) + ". " + str(id))

def printAllEntries(data_dict: dict):
    for index, id in enumerate(data_dict):
        person = data_dict[id]
        printEntry(person, index) 

def printEntryByIndex(data_list: list):
    index = input("Please enter the index of the entry you want to print: ")
    index = mustBeNumberCheck("Index", index)
    last_index = len(data_list) -1
    if index > last_index:
        print("Error: Index out of range. The maximum index allowed is " + str(last_index))
    else:
        person = data_list[index]
        printEntry(person) 

def saveAllData(data_list: list):
    output_csv = input("What is your output file name? ")
    attributes = set()
    for person in data_list:
        for attribute in vars(person).keys():
            attributes.add(attribute)
    attributes = list(attributes)
    all_data = []
    for person in data_list:
        person_attributes = {attributes[i].upper().replace("_"," ")[1:]
                             : getattr(person, attribute, None) for i, attribute in enumerate(attributes)}
        all_data.append(person_attributes)
    df = pd.DataFrame(all_data)
    df.to_csv(output_csv, index=False)

def tryExit():
    while True:
        yes_or_no = input("Are you sure? (y/n) ")
        if yes_or_no == "y":
            print("Goodbye!")
            return True
        elif yes_or_no == "n":
            return False
#########################################################################################################################################################################################
# if __name__ == "__main__":        

data_dict = {}
data_list = []
age_average = 0.0
while True:
    try:
        printMenu()
        option = input("Please enter your choice: ")
        option = convertInputToOption(option)
        if option == Option.INVALID_OPTION:
            continue
        if option == Option.SAVE_NEW_ENTRY:
            age_average = saveNewEntry(data_dict, data_list, age_average)
        elif option == Option.SEARCH_BY_ID:
            searchById(data_dict)
        elif option == Option.PRINT_AGE_AVERAGE:
            printAgesAverage(age_average)
        elif option == Option.PRINT_ALL_NAMES:
            printAllNames(data_dict)
        elif option == Option.PRINT_ALL_IDS:
            printAllIds(data_dict)
        elif option == Option.PRINT_ALL_ENTRIES:
            printAllEntries(data_dict)
        elif option == Option.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(data_list)
        elif option == Option.SAVE_ALL_DATA:
            saveAllData(data_list)
        elif option == Option.TRY_EXIT:
            if tryExit() == True:
                break

        endIterationMessage()
    except KeyboardInterrupt:
        print("\nYou tried to exit with ctrl+c , nice try.")
    except (OptionException, IdAlreadyExists, InvalidInput) as e:
        print(e)
    # finally:
    #     try:
    #         endIterationMessage()
    #     except KeyboardInterrupt:
    #         print("\nYou tried to exit with ctrl+c , nice try.")