# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 17: Power digit sum
Written by cmdellinger

Usage:
  None

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

## ------
## solution
## ------

import time as t
from operator import add
from num2words import num2words
import re

def number_of_chars(number = 0): # -> int
    ''' returns the quantity of characters in the British text version of the input number '''
    number_words = re.findall(u'[^\W_]+', num2words(number, lang='en_GB'))
    return reduce(add, [len(word) for word in number_words])

maximum_number = 1000
total_chars = 0

for integer in xrange(1,maximum_number+1):
    total_chars += number_of_chars(integer)

print "total characters:", total_chars

# print runtime of script
print "script runtime:", t.clock()
