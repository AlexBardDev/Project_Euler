"""
problem: https://projecteuler.net/problem=12
"""

import math

list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def search_primes(list_primes):
    """Function that finds the prime numbers"""

    m = 2
    while True:

        is_prime = True
        possible_prime = list_primes[-1] + m

        for n in range(3, math.ceil(possible_prime/2)):
            if (possible_prime%n) == 0:
                is_prime = False
                break

        if is_prime == True:
            list_primes.append(possible_prime)
            break
        else:
            m += 2

def search_triangular_number(nb):
    """Search a new triangular number"""

    list_nb = [i for i in range(1, nb+1)]

    return sum(list_nb)

def search_number_of_divisors(nbre, list_primes):
    """Search all the divisors of a number"""

    list_factors = []
    i = 0

    #Prime factors
    while True:
        if i >= len(list_primes):
            search_primes(list_primes)

        if nbre%list_primes[i] == 0:
            list_factors.append(list_primes[i])
            nbre = nbre/list_primes[i]
        else:
            i += 1

        if nbre in list_primes or nbre == 1:
            list_factors.append(nbre)
            break


    #Number of divisors
    list_p = []
    t = 0

    while True:
        f = list_factors[0]
        list_p.append(list_factors.count(f))
        for i in range(1, list_p[t]+1):
            list_factors.remove(f)
        t += 1
        if len(list_factors) == 0:
            break

    list_p = [(elt+1) for elt in list_p]

    product = 1
    for elt in list_p:
        product *= elt

    return product

Xth_triangular_number = 3

while True:

    Xth_triangular_number += 1
    tri_nb = search_triangular_number(Xth_triangular_number)
    k = search_number_of_divisors(tri_nb, list_primes)

    if k > 500:
        print(tri_nb)
        break
