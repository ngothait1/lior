from Person import Person
from input_validation import mustBeNumberCheck
from project_exceptions import IdAlreadyExists, InvalidInput

# Inheritance Syntax
class Student(Person):
    def __init__(self):
        super().__init__()
        try:
            self._field_of_study = input("Field of study: ")
            self._year_of_study = input("Year of study: ")
            self._year_of_study = mustBeNumberCheck("Year of study", self._year_of_study)
            self._score_avg = input("Score average: ")
            self._score_avg = mustBeNumberCheck("Score average", self._score_avg)

        except InvalidInput as e:
            Person.all_persons.pop(self._id, None)
            raise e
        
        Person.all_persons[self._id] = super().getName(), super().getAge()

    def getFieldOfStudy(self):
        return self._field_of_study

    def getYearOfStudy(self):
        return self._year_of_study    

    def getScoreAvg(self):
        return self._score_avg

    def getPersonDetails(self):
        details = super().getPersonDetails()
        details.append(self.getFieldOfStudy())
        details.append(self.getYearOfStudy())
        details.append(self.getScoreAvg())
        return details

    def printPerson(self, index = None):
        super().printPerson(index)
        print("\tField of Study: " + self.getFieldOfStudy())
        print("\tYear of Study: " + str(self.getYearOfStudy()))
        print("\tScore average: " + str(self.getScoreAvg()))
        

if __name__ == "__main__":
    # student1 = Student(1, "Charlie", 22, "Computer Science", 3, 88.5)
    # student1.printPerson()
    
    try:
        student2 = Student()
        student2.printPerson()
        student3 = Student()
        student3.printPerson()
        print(Person.all_persons)
    except (InvalidInput, IdAlreadyExists) as e:
        print(e)