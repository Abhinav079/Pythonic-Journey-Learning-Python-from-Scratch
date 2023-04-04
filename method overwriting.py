class Animal:
    def eat(self):
        print("The animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("Rabbit machan is eating") #method eat is overwritten

rabbit=Rabbit()
rabbit.eat()               