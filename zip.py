#the zip() function is used to combine multiple iterables (e.g., lists, tuples, or sets) into a single iterable of tuples. 
#Each tuple contains the corresponding elements from all the input iterables.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]


person_info = dict(zip(names, ages))

print(person_info)
for key,value in person_info.items():
    print(key ,':' ,value)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
