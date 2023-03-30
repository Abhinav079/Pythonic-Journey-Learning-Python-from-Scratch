#In Python, a tuple is an ordered collection of elements, similar to a list.
# However, unlike lists, tuples are immutable, which means you cannot modify their contents once they are created.
my_tuple = ('apple', 'banana', 'orange')
print(my_tuple)
#You can access individual elements in a tuple using indexing, just like with a list:
my_tuple = ('apple', 'banana', 'orange')
print(my_tuple[0])  # 'apple'
print(my_tuple[1])  # 'banana'
#You can also use slicing to access a subset of the elements in a tuple:
my_tuple = ('apple', 'banana', 'orange', 'pear', 'kiwi')
print(my_tuple[1:4])  # ('banana', 'orange', 'pear')
my_tuple = ('apple', 'banana', 'orange')
#my_tuple[1] = 'pear'  # This will raise a TypeError
