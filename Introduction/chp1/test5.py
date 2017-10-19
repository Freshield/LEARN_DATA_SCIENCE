import datetime as dt
import time as tm

print(tm.time())

dtnow = dt.datetime.fromtimestamp(tm.time())

print(dtnow)

print(dtnow.year)
print(dtnow.month)
print(dtnow.second)

delta = dt.timedelta(days=100)
print(delta)

today = dt.date.today()
print(today-delta)
print(today > today - delta)