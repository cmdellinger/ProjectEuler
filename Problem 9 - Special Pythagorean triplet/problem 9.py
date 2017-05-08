# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 9: Special Pythagorean triplet
Written by cmdellinger

Usage:
  None

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

## ------
## solution
## ------

from operator import add
from operator import mul
import time as t

pyth_list = [0, 0, 0]

def find_1000(pyth_list):
    for a in xrange(1, 1000):
        pyth_list[0] = a
        for b in xrange(1, 1000):
            pyth_list[1] = b
            pyth_list[2] = (a**2 + b**2)**0.5
            if reduce(add, pyth_list) == 1000:
                return

find_1000(pyth_list)
pyth_list[2] = int(pyth_list[2])

print "list [a,b,c]:", pyth_list
print "product:", reduce(mul, pyth_list)
print "script runtime:", t.clock()
