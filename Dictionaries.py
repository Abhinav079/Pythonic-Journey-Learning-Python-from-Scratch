#a dictionary is an unordered collection of key-value pairs. The keys in a dictionary must be unique and immutable (strings, numbers, or tuples), and the values can be of any data type (strings, numbers, lists, tuples, other dictionaries, etc.
#You can create a dictionary in Python by enclosing a comma-separated list of key-value pairs inside curly braces {}:
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict)

#You can access the value associated with a key in a dictionary using square brackets [] and the key:
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict['banana'])  # 2

#You can also use the get() method to retrieve the value associated with a key. This method allows you to specify a default value to return if the key is not found in the dictionary:
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.get('pear'))  # 0 (because 'pear' is not in the dictionary)

#You can add or modify a key-value pair in a dictionary by assigning a value to the key
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
my_dict['pear'] = 4  # Add a new key-value pair
my_dict['orange'] = 5  # Modify an existing value
print(my_dict)

#You can also remove a key-value pair from a dictionary using the del statement:
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
del my_dict['banana']
print(my_dict)

#In addition, dictionaries have several useful methods for working with keys, values, and items
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# Get a list of all keys
print(my_dict.keys())  # ['apple', 'banana', 'orange']

# Get a list of all values
print(my_dict.values())  # [1, 2, 3]

# Get a list of all key-value pairs as tuples
print(my_dict.items())  # [('apple', 1), ('banana', 2), ('orange', 3)]
