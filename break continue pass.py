import time
n=5
for i in range(n):
    print(i)
    if i ==3:
        break
for i in range(n):
    if i == 3:
        pass 
        time.sleep(10)   
    print(i)
for i in range(n):
    if i == 3:
        continue
    print(i)