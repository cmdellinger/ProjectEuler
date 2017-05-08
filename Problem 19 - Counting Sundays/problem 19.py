# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 19: Counting Sundays
Written by cmdellinger

Usage:
  None

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

## ------
## solution
## ------

import time as t
from calendar import monthrange

# date ranges
months = [1,12]
years = [1901, 2000]
# counter
first_Sundays = 0

for year in xrange(years[0],years[1]+1):
    for month in xrange(months[0],months[1]+1):
        if monthrange(year,month)[0] == 6:
            first_Sundays += 1

print "First Sundays:", first_Sundays

# print runtime of script
print "script runtime:", t.clock()
