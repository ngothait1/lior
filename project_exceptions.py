class OptionException(Exception):   
    def __init__(self,option):
        super().__init__()
        self._option = option 
    
    def getOption(self):
        return self._option
    
    def __str__(self):
        return f"Error: Option [{self.getOption()}] does not exist. Please try again"

class InvalidInput(ValueError):
    def __init__(self, category: str, value:str):
        super().__init__()
        self._category = category
        self._value = value
    
    def getCategory(self):
        return self._category
    
    def getValue(self):
        return self._value
    
    def __str__(self):
        return f"Error: {self.getCategory()} must be a number. {self.getValue()} is not a number"

class IdAlreadyExists(Exception):
    def __init__(self, name, age):
        super().__init__()
        self._age = age
        self._name = name
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def __str__(self):
        return f"Error ID already exists: name: {self.getName()}, age: {self.getAge()}"
    
if __name__ == "__main__":
    try:
        # raise OptionException("e")
        # raise InvalidInput("Age", "e")
        raise IdAlreadyExists("Lior", "27")
    except OptionException as OE:
        print(OE)
    except InvalidInput as II:
        print(II)
    except IdAlreadyExists as IAE:
        print(IAE)