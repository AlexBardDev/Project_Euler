"""
problem:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import math

K = 10001
LIST_PRIME_NUMBERS = [2, 3, 5]
M = 2

while len(LIST_PRIME_NUMBERS) < K:

    is_prime = True

    MAYBE_PRIME = LIST_PRIME_NUMBERS[-1] + M
    for nb in range(3, math.ceil(MAYBE_PRIME/2)):
        if MAYBE_PRIME%nb == 0:
            is_prime = False
            break  #Not a prime number

    if is_prime == True:
        LIST_PRIME_NUMBERS.append(MAYBE_PRIME)
        M = 2
    else:
        M += 2

print(LIST_PRIME_NUMBERS[-1])
