class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


dogesh = Dog()

dogesh.bark()