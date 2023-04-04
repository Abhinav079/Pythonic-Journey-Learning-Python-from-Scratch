#multilevel inheritance = when a derived call inherits another derived (child) class

class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive) #inherited from the organism class
dog.eat()        #inherited from the animal class
dog.bark()       #inherited in dog class



