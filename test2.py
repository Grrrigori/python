# import calendar
#
# print(calendar.month(2020, 11, w=4, l=0))
#
# # print(calendar.calendar(2020, w=1, l=1, c=15, m=4))
#
#
# print(calendar.TextCalendar.prmonth(theyear= 2021, themonth= 2, w=1, l =1))
#
#
#
# import time
# print(time.asctime())
# print(time.gmtime())
# print(type(time.gmtime()))
#
# now = time.gmtime()
# print(now[0], now[1], now[2])
# start = time.time()
# counter= 0
# while counter <1000000:
#     print('Hello')
#     counter += 1
# end = time.time()
# # time.sleep(7)
#
# end = time.time()
#
# print(end-start)

import datetime

d = datetime.date(2020,7,22)
print(d)
today = datetime.date.today()
print(today)
some_date = datetime.date(2020,6,12)
# tdelta = datetime.timedelta(days= 7)
# print(today + tdelta)
# delta ne data a raznica vo vremeni
# date2 = date1 + timadelta
# timedelta= date1-date2
# the_day = datetime.date(2007,3,28)
# time= today -the_day
# print(time)
#
# bday = datetime.date(2021, 5, 4)
# till_bday= bday-today
# print(till_bday)
