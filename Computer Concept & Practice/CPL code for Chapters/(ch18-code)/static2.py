class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def changeName(self, newName):
        if Person.isValidName(newName):
            self.name = newName
    def changeAge(self, newAge):
        ...
    @staticmethod
    def isValidName(name): pass