#scope = region in which the code is recohnized
#        Avariable is only availale form the region from which it is created
#        A global and locally scoped version of a variable can be created

name = "abhi"#globally scope(available inside amd outside the function)

def display_name():
    name="abhinav"
    print(name)

print(name) #abhi
display_name() #abhinav