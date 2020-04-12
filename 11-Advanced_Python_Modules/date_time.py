import datetime

t = datetime.time(5, 15, 45)

print(t) # 05:15:45
print(t.hour) # 5
print(datetime.time()) # 00:00:00
print(datetime.time.min) # 00:00:00
print(datetime.time.max) # 23:59:59.999999
print(datetime.time.resolution) #0:00:00.000001

today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.year)

print(datetime.date.min) # 0001-01-01
print(datetime.date.max) # 9999-12-31

d1 = datetime.date(2020, 4, 13)
d2 = d1.replace(year=2021)

print(d2 - d1)