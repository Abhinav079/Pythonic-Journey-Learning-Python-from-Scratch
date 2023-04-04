from Car import Car

car1=Car("Chevy","Corvette","2021","blue")
print(car1.make)
print(car1.year)
print(car1.color)
print(car1.model)
car1.drive()
car2=Car("Ford","Mustang","2022","pink")
car2.stop()
Car.wheels = 2
print(car1.wheels)