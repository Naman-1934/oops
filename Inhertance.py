### Base Class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound") 

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks") 

# Create an instance of an Animal

animal = Animal("Generic Animal")
animal.speak() # Output: Generic animal makes a sound

# create an instance of a Dog
dog = Dog("Buddy")
dog.speak() # Output: Buddy barks