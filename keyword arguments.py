#keyword arguments = arguments preceded by an identifier when we pass them to a function
#                    the order of the arguments doesnt matter,unlike positional arguments
#                    python knows the name f the arguments that our function recieves 

def hello(first,middle,last):
    print("Hello "+first+""+middle+" "+last)


print("abhinav","k","EIE") 
#but now if we change the orderof the input then the outcome will change    

def hello(first,middle,last):
    print("Hello "+first+""+middle+" "+last)


print("k","EIE","abhinav") 
#the output in the order changes
#we can use keyword arguments in this case
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)


hello(last="EIE",middle="k",first="abhinav") 
