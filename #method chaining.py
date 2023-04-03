#method chaining =calling multiple methods sequentially

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You stop on the brakes")
        return self
    def turn_off(self):
        print("You tun off the engine")
        return self
    
car = Car()
car.turn_on().drive().brake().turn_off()    

