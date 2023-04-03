#index operator[] = give access to a sequence's element{str,list,tuples}
name="abhinav"

if(name[0].islower()):
    name=name.capitalize()
   
print(name)
first_name=name[0:3].upper()
last_name=name[4:].capitalize()
last_character=name[-1]

print(first_name)
print(last_name)
print(last_character)