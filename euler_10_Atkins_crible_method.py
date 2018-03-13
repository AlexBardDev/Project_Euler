"""
problem: https://projecteuler.net/problem=10
"""

import math

def search_primes(nbre):
    """Function that finds the prime numbers with the Atkins crible"""

    list_primes = []

    #Below 60 at the beginning
    list_maybe_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                         29, 31, 37, 41, 43, 47, 53, 59]

    list_maybe_prime1 = []
    list_maybe_prime2 = []
    list_maybe_prime3 = []

    for elt in range(61, nbre+1, 2):
        if elt%60 in [1, 13, 17, 29, 37, 41, 49, 53]:
            list_maybe_prime1.append(elt)
        elif elt%60 in [7, 19, 31, 43]:
            list_maybe_prime2.append(elt)
        elif elt%60 in [11, 23, 47, 59]:
            list_maybe_prime3.append(elt)

    for n in list_maybe_prime1:
        list_solutions = []
        for x in range(1, math.ceil(math.sqrt(n/4))):
            y = math.sqrt(n-(4*(x**2)))
            if math.trunc(y) == y:
                list_solutions.append((x, y))

        if len(list_solutions)%2 != 0:
            list_maybe_primes.append(n)

    for n in list_maybe_prime2:
        list_solutions = []
        for x in range(1, math.ceil(math.sqrt(n/3))):
            y = math.sqrt(n-(3*(x**2)))
            if math.trunc(y) == y:
                list_solutions.append((x, y))

        if len(list_solutions)%2 != 0:
            list_maybe_primes.append(n)

    for n in list_maybe_prime3:
        list_solutions = []
        x = math.floor(math.sqrt(n/3))
        while True:
            x += 1
            y = math.sqrt((3*(x**2))-n)
            if math.trunc(y) == y and x > y:
                list_solutions.append((x, y))
            if y > x:
                break

        if len(list_solutions)%2 != 0:
            list_maybe_primes.append(n)

    list_maybe_primes = sorted(list_maybe_primes)

    for prime in [2, 3, 5]:
        list_primes.append(prime)
        list_maybe_primes.remove(prime)

    search = True
    while search:

        prime = list_maybe_primes[0]

        list_primes.append(prime)
        list_maybe_primes.remove(prime)
        for elt in list_maybe_primes:
            if elt%(list_primes[-1]**2) == 0:
                list_maybe_primes.remove(elt)

        if (list_maybe_primes[0]**2) > list_maybe_primes[-1]:
            list_primes += list_maybe_primes
            search = False

    return list_primes

print(sum(search_primes(2000000)))
