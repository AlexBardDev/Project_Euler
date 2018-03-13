"""
problem: https://projecteuler.net/problem=21
"""

import math

def sum_divisor(nb):
    """Function that finds all the divisors of a number and return the sum"""

    return sum([elt for elt in range(1, (math.ceil(nb/2))+1) if nb%elt == 0])

list_amicable_numbers = []
list_numbers = range(1, 10001)
i = 0

while i < len(list_numbers):
    k = sum_divisor(list_numbers[i])
    if k != list_numbers[i] and sum_divisor(k) == list_numbers[i] and k not in list_amicable_numbers:
        list_amicable_numbers.append(list_numbers[i])
        list_amicable_numbers.append(k)
    i += 1

print(sum(list_amicable_numbers))
