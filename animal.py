# blueprint for the animal class, what it could be, what it could do, what attributes it has, what methods it has
class Animal:
    """
    Base class representing a generic animal.
    """

    # class level parameter or attribute
    kingdom = "Animalia"


    # object specific attributes constructor initializer what you need to build the object
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # class method, what the animal can do, what it can say
    def speak(self):
        print(f"{self.name} makes a noise.\n")

    # magic method, how print object behaves. override the behavior of the object
    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
            f"Name: {self.name}\n"
            f"Species: {self.species}\n")


