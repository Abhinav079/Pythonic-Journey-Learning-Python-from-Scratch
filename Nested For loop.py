#Nested loop - this loop is used to print patterns for each outer loop the inner loop runs n times

n=input("Enter the symbol: ")
r=int(input("Enter the no of rows: "))
c=int(input("Enter the no of coloumns: "))
for i in range(c):
    for j in range(r):
        print(n,end="")
    print()    