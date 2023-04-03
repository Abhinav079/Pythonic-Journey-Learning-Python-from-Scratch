#functions = a block of code which is executed only when it is called.
def hello():
    print("hello!")
    print("Have a nice day")

hello()    

def hello(name):#Argument passing
    print("hello!"+name)
    print("Have a nice day!")

my_name="abhi"
hello(my_name)    

#passing multiple arguments
def hello(first_name,last_name):
    print("hello!"+first_name+''+last_name)
    print("Have a nice day!")

hello("abhinav","k")

#passing multiple argumnets with different datatypes
def hello(first_name,last_name,age):
    print("hello!"+first_name+''+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("abhinav","k",18)

#return statements = functions send python values /objects back to the caller
# These values /objects are known as the functions return value
def multiply(num1,num2):
    result = num1*num2
    return result

multiply(6,8)#we cant get answer we have to print it
print(multiply(6,8))
