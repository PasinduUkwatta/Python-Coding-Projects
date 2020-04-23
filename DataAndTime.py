import time
print(time.time())
print(time.ctime(1586414139.4928787))
a=time.localtime()
print(time.mktime(a))



print(a)
help('time.strftime')
print(time.strftime("%Y :%m :%d :%B"))

import datetime

#printing the given date
a = datetime.datetime(2020,4,9,12,24,45,789)
print(a)

#printing the curreny date
b = datetime.datetime.today()
print(b)
c = datetime.datetime.now()
print(c)

#getting selected ones only

d=b.year
e=b.month
f=b.time()

print('year is ',d,
      'month is ',e,
      'time is ',f)

d1 = datetime.timedelta(days=20,hours=30)
d2 = datetime.timedelta(days=13,hours=48)

d3= d1-d2
print(d3)
print(type(d3))