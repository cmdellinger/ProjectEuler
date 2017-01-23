"""
ProjectEuler Problem 7: 10001st prime
Written by cmdellinger

Usage:
  None

Find the 10 001st prime number.
"""

## ------
## solution
## ------

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

prime_count = 1 # already includes 2 as a prime
test_number = 1 # start at 1 so loop starts at 3

while prime_count < 10001:
    test_number += 2 # excludes numbers divisible by 2
    prime_count += is_prime(test_number)

print test_number
