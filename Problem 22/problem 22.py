# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 22: Names scores
Written by cmdellinger

Usage:
  None

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

## ------
## solution
## ------

import time as t
from operator import add
import re

def char_to_AZ_value(character = ''): # -> int
    ''' takes in character as a string and returns the corresponding 1-26 value for A-Z '''
    return ord(character.upper())-64

def name_to_AZ_value(name = ''): # -> int
    ''' takes in a name and returns the sum of the letter character values (1-26 for A-Z) '''
    return sum([char_to_AZ_value(letter) for letter in name])

# import name name list from file
with open('names.txt', 'r') as inputfile:
    name_list = sorted(re.findall(u'[^\W_]+', inputfile.readline()))

total = 0
for index in xrange(len(name_list)):
    total += name_to_AZ_value(name_list[index])*(index+1)

print "total of name scores:", total

# print runtime of script
print "script runtime:", t.clock()
