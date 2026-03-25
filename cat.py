from animal import Animal

class Cat(Animal):
    """
    Derived class representing a cat which is a type of animal.
    """
    
    def __init__ (self, name, species, color):
        super(). __init__(name, species)
        self.color = color
        
    def __str__(self):
        return super(). __str__ () + f"Color: {self.color}\n"
    
    def speak(self):
        print (f"{self.name} Meow!")