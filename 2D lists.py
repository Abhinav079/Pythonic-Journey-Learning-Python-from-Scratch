#2Dlists - this is a list inside a list
household_things=[['apple','orange',"grape"],['brush','paste'],['gram','dhal']]
try:
    print(household_things)
    k=int(input('enter row of which product you want: '))
    l=int(input('Enter coloumn of product you want: '))
    print(household_things[k][l])
except IndexError as e:
    print(e)
    print("please print valid index")