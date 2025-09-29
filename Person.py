from project_exceptions import InvalidInput, IdAlreadyExists
from input_validation import mustBeNumberCheck

class Person():
    all_persons = {}
    
    def __init__(self):
        self._id = input("ID: ")
        self._id = mustBeNumberCheck("ID", self._id)
        if self._id in Person.all_persons:
            name, age = Person.all_persons[self._id]
            raise IdAlreadyExists(name, age)
        else:
            self._name = input("Name: ")
            self._age = input("Age: ")
            self._age = mustBeNumberCheck("Age", self._age)
            Person.all_persons[self._id] = [self._name, self._age]
    
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def setID(self, id):
        self._id = id
    
    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age
    
    def getPersonDetails(self):
        return [self.getID(), self.getName(), self.getAge()]
    
    def getPersonString(self):
        #better to use getter even inside class
        return f"The person {self.getName()} is {self.getAge()} years old and he has ID {self.getID()},"
    
    def printPerson(self, index = None):
        if index != None:
            print(str(index) + ". " + str(self.getID()))
        else:
            print("ID: " + str(self.getID()))
        print("\tName: " + self.getName())
        print("\tAge: " + str(self.getAge()))
    
    def getAllPersons():
        return Person.all_persons
        
           
if __name__ == "__main__":
    person1 = Person()
    person1.printPerson()
    person2 = Person()
    person2.printPerson(2)
    
    if person1.getName() != "Alice":
        print(f"Error name should be Alice not {person1.getName()}")
    if person1.getAge() != 30:
        print(f"Error age should be 30 not {person1.getAge()}")

    all_persons = Person.getAllPersons()

    if list(all_persons.keys()) != [1,2]:
        print(f"Error id values should be [1,2] not {list(all_persons.keys())}")

    try:    
        p3 = Person()
        p3.printPerson()
        p4 = Person()
    except (InvalidInput, IdAlreadyExists) as e:
        print(e)
    