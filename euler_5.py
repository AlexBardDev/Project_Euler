"""
problem:

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
"""

import math

def PPCM(a, b):
    """Function that finds the smallest common multiple"""

    return int((a*b)/(math.gcd(a, b)))

t = 1
k = 2
while k <= 20:
    t = PPCM(t, k)
    k += 1

print(t)
