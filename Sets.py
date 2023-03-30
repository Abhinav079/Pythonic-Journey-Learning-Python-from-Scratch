#a set is an unordered collection of unique elements. The elements in a set must be immutable, which means they cannot be changed once they are added to the set.
#You can create a set in Python by enclosing a comma-separated list of elements inside curly braces {}. Alternatively, you can use the built-in set() function to create a set.
#Here are some examples:
# Creating a set using curly braces
my_set = {'apple', 'banana', 'orange'}
print(my_set)

# Creating a set using the set() function
my_set = set(['apple', 'banana', 'orange'])
print(my_set)

my_set = {'apple', 'banana', 'orange'}
print('apple' in my_set)  # True
print('pear' in my_set)  # False

my_set = {'apple', 'banana', 'orange'}
my_set.add('pear')
print(my_set)

my_set.remove('banana')
print(my_set)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union
print(set1.union(set2))  # {1, 2, 3, 4}

# Intersection
print(set1.intersection(set2))  # {2, 3}

# Difference
print(set1.difference(set2))  # {1}
