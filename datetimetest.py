import time
import calendar
ticks = time.time()
print ("current time = ", ticks)
gmttime = time.gmtime(time.time())
localtime = time.localtime(time.time())
fmtgmttime = time.asctime(gmttime)
fmtlocaltime = time.asctime(localtime)
print(fmtgmttime)
print(fmtlocaltime)
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",gmttime))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

c= calendar.month(2023,11)
print(c)