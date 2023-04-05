#it makes decision independent of class

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is talking")

class Chicken:
    def walk(self):
        print("This chick is walking")
    def talk(self):
        print("This chick is talking")         

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
