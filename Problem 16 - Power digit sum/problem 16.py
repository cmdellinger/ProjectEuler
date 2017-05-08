# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 16: Power digit sum
Written by cmdellinger

Usage:
  None

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

## ------
## solution
## ------

import time as t
from operator import add

# number to sum digits
number = 2**1000
# change number to string and create list of chars
digits = list(str(number))
# change chars of numbers in the list back to integers
digits = map(int, digits)
# sum all the elements in the list
sum = reduce(add, digits)

print "sum of digits", sum

'''
# this can be reduced to one long confusing line
print "sum of digits", reduce(add, map(int, list(str(2**1000))))
'''

# print runtime of script
print "script runtime:", t.clock()
