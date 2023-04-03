# Prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class
# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but dont have am implementation

from abc import ABC, abstractmethod

class Vechicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vechicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vechicle):
    def go(self):
        print("You ride the motorcycle")



car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()