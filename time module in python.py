#the time module provides various time-related functions
import time
y=time.time()#time since the epoch
x=print(time.ctime(y))#ctime = current time
y=print(time.time())
print(time.localtime())
x=time.localtime()
print(time.gmtime())
local_time = time.strftime("%B %d %Y %H: %M: %S",x)
print(local_time)
time_tuple = (2020,4,20,4,20,0,0,0,0)
time_str = time.mktime(time_tuple)
print(type(time))
