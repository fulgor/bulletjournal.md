#!/usr/bin/env python

# author: frag.fulgor@gmail.com
# repo: https://github.com/fulgor/bulletjournal.md/scripts/bjmd.py


# IMPORT MODULES
import time
import datetime
import calendar
from calendar import monthrange


# SET VARIABLES
prefix = '    '   # 4 blanks before day in list
suffix = '  '     # 2 blanks after weekday list

# this year or specified year:
now = datetime.datetime.now()
year = now.year
# year = 2022     # or enter specific year

# include (1 = on, 0 = off):
include_keys = 1 
include_calendarmatrix = 0   # experimental

# order (1 = on, 0 = off):
# Soren Kierkegaard: Life can only be understood backwards; but it must be lived forwards.
reversemonth = 1  # 0 = Jan to Dec, 1 = Dec to Jan
reverseday = 1    # 0 = Mon to Sun, 1 = Sun to Mon

# set first day of week:
# calendar.setfirstweekday(calendar.SUNDAY)
calendar.setfirstweekday(calendar.MONDAY)


# DEFINITIONS:

def keys():
    """ Add keys and their meaning to output """
    if include_keys:
       key_str = """
## Keys
    .  task
    .! add priority
    x  done
    o  event
    >  postponed
"""
       print key_str


def createday(day):
    """ Create list of days with date and weekday """
    mydate = datetime.date(year, month, day)  #year, month, day
    datedate = mydate.strftime("%Y-%m-%d %A")
    message = '### {}'.format(datedate)
    print(message)
    print('-' * (len(message)))  # line under name
    print


def createmonth(month):
    """ Create short list of days of month """
    mymonth = datetime.date(year, month, 1)  #year, month, day
    print
    print '##',mymonth.strftime("%B")
    # print('-' * (len(mymonth.strftime("%B"))))  # line under name
    print

    if include_calendarmatrix:
       print(calendar.month(year, month,10,1))  # matrix of month (coloumn distance, lines)

    maxdays = (monthrange(year, month)[1])  # number of days in month

    for day in range(1,maxdays+1):
       mydate = datetime.date(year, month, day)  #year, month, day
       datedate = mydate.strftime("%d %a")
       message = '{}{}{}'.format(prefix, datedate, suffix)
       print(message)
    print

    if reverseday:
       for day in range(maxdays, 0, -1):
           createday(day)
    else:
       for day in range(1,maxdays+1):
          createday(day)

    print


# WORKFLOW:

# create calendar and list of days for each month of year:
print '#',year

if include_keys:
   keys()

if reversemonth:
   for month in range(12, 0, -1):        # Dec to Jan: start, stop, step Jan to Dec
      createmonth(month)
else:
   for month in range(1,12+1):                  # Jan to Dec
     createmonth(month)


# eof
