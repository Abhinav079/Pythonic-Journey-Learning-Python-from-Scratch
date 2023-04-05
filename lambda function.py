#Lambda function = function written in 1 line using lambda keyword
#                  accepts any number of arguments, but lately has one expression
#                  (think of it as a a shortcut)
#                  (useful if needed for a short period of time, throw-ack)


#def myfun(f):
#
#     f()
#def x():
#   print('hello)
#myfun(x)

#lambda parameters: expression

double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name,last_name: first_name+" "+last_name
age_check = lambda age:True if age>=10 else False
print(multiply(10,20))
print(double(10))
print(add(10,20,30))
print(full_name("abhinav","karthikeyan"))
print(age_check(10))