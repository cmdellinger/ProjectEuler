# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 20: Factorial digit sum
Written by cmdellinger

Usage:
  None

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

## ------
## solution
## ------

import time as t
from math import factorial

number = 100

factorial = factorial(number)
factorial_sum = sum(map(int, list(str(factorial))))

print "sum of factorial digits for " + str(number) + "!:", factorial_sum


# print runtime of script
print "script runtime:", t.clock()
