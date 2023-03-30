#lists = lists are ordered changeable datatype available in python
mylist=[10,40,20,30,1]
print(mylist)
#methods in list
mylist.append(40)
print(mylist)
mylist.insert(2,"aa")
print(mylist)

mylist.sort()
print(mylist)
print(mylist.index(40))

mylist.reverse()
print(mylist)