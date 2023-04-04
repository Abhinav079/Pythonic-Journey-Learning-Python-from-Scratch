#**Kwargs => parameter that will pack all arguments in a dictionary
#            useful so that a function can accept varying amount of arguments
def hello(**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr",first="abhinav",middele="dude")
        