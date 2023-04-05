# map() is a built-in function that takes in two or more arguments. The first argument is a function, and the second argument is an iterable (such as a list, tuple, or set).
# map() applies the function to each element of the iterable and returns an iterator that produces the results.

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5]
squared_list = map(square, my_list)

print(list(squared_list))
