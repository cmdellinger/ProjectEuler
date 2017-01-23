"""
ProjectEuler Problem 6: Sum square difference
Written by cmdellinger

Usage:
  None

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

## ------
## solution
## ------

def square_of_sums(number = 0): # -> integer
    ''' returns the square of the sums of natural numbers up to input number '''
    sum = 0
    for integer in xrange(1, number + 1):
        sum += integer
    return sum**2

def sum_of_squares(number = 0): # -> integer
    ''' returns the sum of the squares of natural numbers up to input number '''
    sum = 0
    for integer in xrange(1, number + 1):
        sum += integer**2
    return sum

natural_number = 100

print abs(sum_of_squares(natural_number) - square_of_sums(natural_number))
