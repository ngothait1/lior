import os
import pandas as pd
import json

# Helper functions

def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")

def printError(option):
    print("Error: Option [" + option + "] does not exist. Please try again")

def printEntry(id, name, age):
    print("ID: " + str(id))
    print("Name: " + name)
    print("Age: " + str(age))

def endIterationMessage():
    input("Press Enter to continue ")

#############################################################################################################################################################
# Main functions

def saveNewEntry(data_dict, data_list, age_average):
    id = input("ID: ")
    if id.isdigit() == False:
        print("Error: ID must be a number. " + id + " is not a number")
        return
    id = int(id)
    if id in data_dict:
        name, age = data_dict[id] 
        print("Error ID already exists: {'name': '" + name + "', 'age': " + str(age) + "}")
    else:
        name = input("Name: ")
        age = int(input("Age: "))
        num_entries = len(data_dict)
        data_list.append((id, name, age))
        data_dict[id] = (name, age)
        sum_of_ages = num_entries* age_average + age
        age_average = sum_of_ages / (num_entries + 1)
        print("ID [" + str(id) + "] saved successfully")
    return age_average

def searchById(data_dict):
    id = input("Please enter the ID you want to look for: ")
    if id.isdigit() == False:
        print("Error: ID must be a number. " + id + " is not a number")
    elif int(id) not in data_dict:
        print("Error: ID " + id + " is not saved")
    else:
        name, age = data_dict[int(id)] 
        printEntry(id, name, age)

def printAgesAverage(age_average):
    print(age_average)

def printAllNames(data_dict):
    for index, (name, _) in enumerate(data_dict.values()):
        print(str(index) + ". " + name)

def printAllIds(data_dict):
    for index, id in enumerate(data_dict):
        print(str(index) + ". " + str(id))

def printAllEntries(data_dict):
    for index, id in enumerate(data_dict):
        name, age = data_dict[id]
        print(str(index) + ". " + str(id))
        print("\tName: " + name)
        print("\tAge: " + str(age))

def printEntryByIndex(data_list):
    index = input("Please enter the index of the entry you want to print: ")
    if index.isdigit() == False:
        print("Error: Index is not a number or a negative number")
        return
    index = int(index)
    last_index = len(data_list) -1
    if index > last_index:
        print("Error: Index out of range. The maximum index allowed is " + str(last_index))
    else:
        id, name, age = data_list[index]
        printEntry(id, name, age)

def saveAllData(data_list):
    output_csv = input("What is your output file name? ")
    if os.path.exists("conf.json") == False:
        print("Error: Config file conf.json is missing in path " + os.getcwd())
    with open("conf.json") as json_file:
        categories_dict = json.load(json_file)
    column_names = [categories_dict["id"], categories_dict["name"], categories_dict["age"]]
    df = pd.DataFrame(data_list, columns=column_names)
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
    printMenu()
    option = input("Please enter your choice: ")
    if option.isdigit() == False or int(option) > 9:
        printError(option)
        continue
    option = int(option)
    if option == 1:
        age_average = saveNewEntry(data_dict, data_list, age_average)
    elif option == 2:
        searchById(data_dict)
    elif option == 3:
        printAgesAverage(age_average)
    elif option == 4:
        printAllNames(data_dict)
    elif option == 5:
        printAllIds(data_dict)
    elif option == 6:
        printAllEntries(data_dict)
    elif option == 7:
        printEntryByIndex(data_list)
    elif option == 8:
        saveAllData(data_list)
    elif option == 9:
        # option == 9 , or in other words exit
        if tryExit() == True:
            break
        
    
    endIterationMessage()