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

with open('names.txt', 'r') as f:
    names = [name.strip('\"') for name in f.read().split(',')]
names.sort()
name_scores = []
for index, name in enumerate(names):
    position = index + 1
    alpha_score = sum(map(lambda x: ord(x)-64, name))
    name_score = position * alpha_score
    name_scores.append(name_score)
print("sum of all name scores:\n",sum(name_scores))

# print runtime of script
print("script runtime:", t.clock())
