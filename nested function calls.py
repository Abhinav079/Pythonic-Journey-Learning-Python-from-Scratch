#nested function calls = function calls inside other function calls
#                        innermost functon calls are resolc=ved first
#                        returned value is used as argument for the nextouter function

# num = imput("Enter a ehole number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a postive number: ")))))