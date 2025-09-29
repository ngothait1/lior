from Person import Person
from input_validation import mustBeNumberCheck
from project_exceptions import IdAlreadyExists, InvalidInput

# Inheritance Syntax
class Employee(Person):
    def __init__(self):
        super().__init__()
        try:
            self._field_of_work = input("Field of work: ")
            self._salary = input("Salary: ")
            self._salary = mustBeNumberCheck("Salary", self._salary)
        except InvalidInput as e:
            Person.all_persons.pop(self._id, None)
            raise e

        Person.all_persons[self._id] = super().getName(), super().getAge()

    def getFieldOfWork(self):
        return self._field_of_work    

    def getSalary(self):
        return self._salary

    def getPersonDetails(self):
        details = super().getPersonDetails()
        details.append(self.getFieldOfWork())
        details.append(self.getSalary())
        return details
    
    def printPerson(self, index = None):
        super().printPerson(index)
        print("\tField of Work: " + self.getFieldOfWork())
        print("\tSalary: " + str(self.getSalary()))


if __name__ == "__main__":
    try:
        emp2 = Employee()
        emp2.printPerson()
        emp3 = Employee()
        emp3.printPerson()
        print(Person.all_persons)
    except (InvalidInput, IdAlreadyExists) as e:
        print(e)