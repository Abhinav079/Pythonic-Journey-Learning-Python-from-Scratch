#sort()method = used with lists
#sort()functions = used with iterables

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)

students=[("squart","H",60),("sandy","A",33),("Patrick","F",33),("spongebob","C",78)]
age=lambda ages:ages[2]
h = sorted(students, key = lambda x:x[1])
for i in h:
    print(i)
