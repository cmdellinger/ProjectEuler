# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 10: Summation of primes
Written by cmdellinger

Usage:
  None

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

## ------
## solution
## ------

from operator import add
import time as t

def is_prime(number = 0): # -> boolean
    ''' returns whether a number is a prime number or not '''
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for factor in xrange(3, int(number**0.5+1), 2):
        if number % factor == 0:
            return False
    return True

max = 2000000

primes = [x for x in xrange(2,max + 1) if is_prime(x)]
prime_sum = reduce(add, primes)
print prime_sum

# alternate method
'''
def prime(x): return x * is_prime(x)
print reduce(add, map(prime, xrange(2,max + 1)))
'''

print "script runtime:", t.clock()
