"""
ProjectEuler Problem 3: Largest prime factor
Written by cmdellinger

Usage:
  None
  
Find the largest prime factor of the number 600851475143.
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
    for factor in xrange(3, int(number**0.5), 2):
        if number % factor == 0:
            return False
    return True

# initialize largest factor
largest_factor = 0
# initialize upper bound number
check_number = 600851475143

# check range up to squareroot since checking prime-ness of factor pairs
for factor in xrange(2,int(check_number**0.5)):

    # print to display status since this might take a while
    print "checking: " + str(factor)

    # check if a number is a factor
    if check_number % factor == 0:
        # check if the current factor is prime
        if is_prime(factor):
            largest_factor = factor
        # check if other factor of pair is prime
        if is_prime(check_number/factor):
            largest_factor = check_number/factor

# print answer
print "largest prime factor: " + str(largest_factor)
