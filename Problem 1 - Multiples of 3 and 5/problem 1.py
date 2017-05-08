"""
ProjectEuler Problem 1: Multiples of 3 and 5
Written by cmdellinger

Usage:
  None
  
Find the sum of all the multiples of 3 or 5 below 1000.
"""

## ------
## solution
## ------

sum = 0
for integer in xrange(1,1000): # ending bound is exclusive
    if integer % 3 == 0 or integer % 5 == 0:
        sum += integer
print sum
