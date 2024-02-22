#1
from datetime import datetime, timedelta

date = datetime.now()

five_days_ago = date - timedelta(days=5)

print(five_days_ago.strftime("%d"))

#2
from datetime import datetime, timedelta

current_date = datetime.now()

one_day_ago = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(one_day_ago.strftime("%d"))
print(current_date.strftime("%d"))
print(tomorrow.strftime("%d"))

#3
from datetime import*
c = input("Input date in yy-mm-dd format: ")
try:
    b = datetime.strptime(c, "%Y-%m-%d")
    d = b.replace(microsecond = 0)
    print(d)
except ValueError:
    print("Your input is wrong")
    
#4 Write a Python program to calculate two date difference in seconds
from datetime import *
e = input("Input first date in yy-mm-dd format: ")
f = input("Input second date in yy-mm-dd format: ")
try:
    a = datetime.strptime(e, "%Y-%m-%d")
    b = datetime.strptime(f, "%Y-%m-%d")
    difference = b - a
    difference_in_seconds= difference.total_seconds()
    print(difference_in_seconds)
except ValueError:
    print("Your input is wrong")