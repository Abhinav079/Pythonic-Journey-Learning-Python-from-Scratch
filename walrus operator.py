#The walrus operator, also known as the assignment expression, is a new operator introduced in Python 3.8. 
#It is represented by the symbol := and is used to assign a value to a variable as part of an expression.
# Without walrus operator
name = input("Enter your name: ")
if len(name) > 0:
    print(f"Hello, {name}!")
else:
    print("You didn't enter your name.")

# With walrus operator
if (name := input("Enter your name: ")) :
    print(f"Hello, {name}!")
else:
    print("You didn't enter your name.")
