#inheritance = child class can access parent class as used in dna

class Animal:

    alive=True

    def eat(self):
        print("The animal is eating")
        
    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("The rabbit is running")
class Fish(Animal):
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("The hawk is flying")

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

print(rabbit.alive)
fish.eat()

rabbit.run()
fish.swim()
hawk.fly()
