"""
ProjectEuler Problem 2: Even Fibonacci numbers
Written by cmdellinger

Usage:
  None
  
Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
"""

## ------
## solution
## ------

# start sum at 0
sum = 0

# define working Fibonacci range start point
lower_bound = 1
upper_bound = 2

while upper_bound < 4 * 10**6: # using upper bound because 1 is not even
    # if even add to sum
    if upper_bound % 2 == 0:
        sum += upper_bound
    # calculate new upper_bound and then move up the Fibonacci sequence
    next_upper_bound = lower_bound + upper_bound
    lower_bound = upper_bound
    upper_bound = next_upper_bound

# print the answer
print sum
