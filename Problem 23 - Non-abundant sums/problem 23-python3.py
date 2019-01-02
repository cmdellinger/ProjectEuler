# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 23: Non-abundant sums
Written by cmdellinger

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

## ------
## solution
## ------

import time as t

def divisors(number):
    ''' returns the divisors (factors - self) for the input number'''
    factors = [1]
    for integer in range(2, int(number**0.5) + 1):
        if number % integer == 0:
            factors.extend([integer, int(number/integer)])
    return set(factors)

def is_abundant(number):
    ''' returns whether the number passed is abundant '''
    if number < 12:
        return False
    return sum(divisors(number)) > number

limit = 28123
abundant_numbers = set(number for number in range(12,limit+1) if is_abundant(number))

def is_abundant_sum(i):
    ''' returns whether the number passed is the sum of abundant numbers '''
    return any(i-a in abundant_numbers for a in abundant_numbers)

sum_of_non_abundant_sums = sum(number for number in range(1,limit+1) if not is_abundant_sum(number))
print('sum of valid positive integers:', sum_of_non_abundant_sums)
# print runtime of script
print("script runtime:", t.clock())
