# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 14: Longest Collatz sequence
Written by cmdellinger

Usage:
  None

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

## ------
## solution
## ------

import time as t

# collatz_sequence() not used:
# building and keeping track of the sequence ends up being slower
def collatz_sequence(number = 0):
    ''' returns the collatz sequence that starts with the inputed number '''
    sequence = [number]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1]/2)
        else:
            sequence.append(3*sequence[-1] + 1)
    return sequence

def collatz_sequence_length(number = 0): # -> int
    ''' returns the length of the collatz sequence that starts with the inputed number '''
    # initialize sequence counters
    index = 1
    element = number
    # increment sequence index and find next element
    while element != 1:
        index += 1
        if element % 2 == 0:
            element /= 2
        else:
            element = 3*element + 1
    # return the length of the sequence
    return index

# initialize values to test less than maximum and keep track of longest sequence length
maximum = 1000000 # exclusive maximum
longest = [0,0] # [staring number, sequence length]
# check collatz sequence length for test all values less than maximum
for number in range(1,1000000):
    print "currently testing:", number
    length = collatz_sequence_length(number)
    if length > longest[1]:
        longest = [number,length]

#print longest sequence and what number (index) starts the longest sequence
print "longest sequence:", longest[1], "for index:", longest[0]

# print runtime of script
print "script runtime:", t.clock()
