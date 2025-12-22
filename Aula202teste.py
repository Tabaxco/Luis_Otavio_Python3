class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name, "is barking")
    
    @staticmethod
    def info():
        print("Dogs are mammals")
    
    @classmethod
    def species(cls):
        print("Species: Canis lupus familiaris")

Atom = Dog('Atom')
Atom.bark()
Atom.info()
Atom.species()

class Person(Dog):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, text):
        name, age = text.split('-')
        return cls(name, int(age))

jonas = Person

jonas.species()