"""
ProjectEuler Problem 4: Largest palindrome product
Written by cmdellinger

Usage:
  None
  
Find the largest palindrome made from the product of two 3-digit numbers.
"""

## ------
## solution
## ------

def is_palindrome(number = 0): # -> boolean
    number_string = str(number)
    for i in xrange(0,len(number_string)/2):
        if number_string[i] != number_string[-(i+1)]:
            return False
    return True

largest_palindrome = 0
largest_factor_1 = 0
largest_factor_2 = 0

for factor_1 in xrange(999, 99, -1):
    for factor_2 in xrange(999, 99, -1):
        if is_palindrome(factor_1 * factor_2):
            palindrome = factor_1 * factor_2
            if palindrome > largest_palindrome:
                largest_palindrome = palindrome
                largest_factor_1 = factor_1
                largest_factor_2 = factor_2

print "largest palindrome", largest_palindrome
print "factors:", largest_factor_1, largest_factor_2
