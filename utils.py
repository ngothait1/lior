from Person import Person
from Student import Student
from Employee import Employee
from input_validation import mustBeNumberCheck
from project_exceptions import IdAlreadyExists, InvalidInput

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

def getProfile():
    profile = input("Please enter the profile you want to create (0 - Person, 1 - Student, 2 - Employee): ")
    profile = mustBeNumberCheck("Profile", profile)
    if profile > 2:
        print(f"Error: {profile} is illegal profile.")
        return None
    
    person_types = [Person, Student, Employee]
    return person_types[profile]()
    # if profile == "Employee":
    #     return Employee()
    # elif profile == "Student":
    #     return Student()
    # elif profile == "Person":
    #     return Person()
    # else:
    #     print("Error: " + profile + " is illegal profile.")
    #     print("Profile should be Person or Student or Employee")
    #     return None

def printEntry(person, index:int = None):
    person.printPerson(index)
        
def endIterationMessage():
    input("Press Enter to continue ")