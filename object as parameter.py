class Car:

    color = None

def color_change(vechicle,color):

    vechicle.color=color

car1=Car()
car2=Car()
car3=Car()        

color_change(car1,"WHITe")
color_change(car2,"Meganda")
color_change(car3,"Violet")

print(car1.color)
print(car2.color)
print(car3.color)