# -*- coding: UTF-8 -*-

# python version 3.5

"""
ProjectEuler Problem 21: Amicable numbers
Written by cmdellinger

Usage:
  None

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

## ------
## solution
## ------

import time as t
from math import factorial

def find_factors(number = 0): # ->  []
    ''' returns a list of factors for the input number '''
    # create list of factor pairs
    factors = [[integer, number/integer] for integer in range(1, int(number**0.5) + 1) if number % integer == 0]
    # flatten list
    factors = [item for sublist in factors for item in sublist]
    # return sorted list
    return sorted(factors)

def d(number = 0):
    ''' returns the d() value for the number provided.
        d() is the sum of all the traditional factors except the number itself. '''
    return sum(find_factors(number)) - number

def amicable_pair(number = 0):
    ''' returns the amicable pair including the input number or zero (False) if not a pair '''
    pair = d(number)
    if number == d(pair) and number != pair:
        return [number, pair]
    else:
        return 0

''' start of calculation sequence '''
max_number = 10000 # exclusive
amicable_numbers = [] # we'll store the pair to prevent duplicates

for number in range(1,max_number):
    if number not in amicable_numbers:
        pair = amicable_pair(number)
        if pair:
            amicable_numbers.extend(pair)

print("sum of all amicable number under " + str(max_number) + ":", sum(amicable_numbers))

# print runtime of script
print("script runtime:", t.clock())
