# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 18: Maximum path sum I
Written by cmdellinger

Usage:
  None

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

## ------
## solution
## ------

import time as t

''' build the triangle '''

num_string = '\
    75\
    95 64\
    17 47 82\
    18 35 87 10\
    20 04 82 47 65\
    19 01 23 75 03 34\
    88 02 77 73 07 63 67\
    99 65 04 28 06 16 70 92\
    41 41 26 56 83 40 80 70 33\
    41 48 72 33 47 32 37 16 94 29\
    53 71 44 65 25 43 91 52 97 51 14\
    70 11 33 28 77 73 17 78 39 68 17 57\
    91 71 52 38 17 14 91 43 58 50 27 29 48\
    63 66 04 68 89 53 67 30 73 16 69 87 40 31\
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

# take text and split into a list, splitting by " ",
# then make string numbers into integers
num_list = map(int, num_string.split())

def triangle_number(number = 0):
    ''' returns value in triangle number sequence at input location '''
    sum = 0
    try:
        for integer in xrange(1,number +1):
            sum += integer
    except:
        pass
    return sum

levels = 0
while triangle_number(levels)/ len(num_list) != 1:
    levels += 1

triangle = []
for level in xrange(0,levels):
    start = triangle_number(level)
    end = triangle_number(level+1)
    triangle.append(num_list[start:end])

''' solve the problem '''

def go_direction(row = 0, column = 0):
    ''' uses recursion to add current value and max of left and right trees '''
    try:
        return triangle[row][column] + max(go_direction(row+1, column), go_direction(row+1, column+1))
    except:
        return 0

print "largest path:", go_direction(0,0)

# print runtime of script
print "script runtime:", t.clock()
