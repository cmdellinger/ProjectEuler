"""
ProjectEuler Problem 5: Smallest multiple
Written by cmdellinger

Usage:
  None
  
Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
"""

## ------
## solution
## ------

# this works but needs optimization

def divisible_1_to_20(number = 0): # -> boolean
    for divisor in xrange(1,20 + 1):
        if number % divisor != 0:
            return False
    return True

number = 0
i = 0

while number == 0:
    i += 1
    if divisible_1_to_20(i):
        number = i

print number
