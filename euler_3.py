"""
problem :

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def find_prime_number(list_numbers_already_primes):
    """Function that finds the new prime number"""

    m = 2
    while True:
        is_prime = True

        #A new prime number
        MAYBE_PRIME = list_prime_numbers[-1] + m

        for nb in range(2, MAYBE_PRIME):
            if MAYBE_PRIME%nb == 0:   #Check that MAYBE_PRIME has no multiples
                is_prime = False

        #If MAYBE_PRIME has no multiples, so MAYBE_PRIME is a prime number
        if is_prime == True:
            list_prime_numbers.append(MAYBE_PRIME)
            break
        else:
            m += 2

NUMBER = 600851475143

list_prime_numbers = [2, 3]
list_prime_factors = []

K = -1
ACTIVE = True

while ACTIVE:
    K += 1

    #k is out of range, we need a new prime number
    if K >= len(list_prime_numbers):
        find_prime_number(list_prime_numbers)

    #Check that NUMBER has a multiples
    if NUMBER%list_prime_numbers[K] == 0:
        list_prime_factors.append(list_prime_numbers[K])
        NUMBER = NUMBER/list_prime_numbers[K]

    if NUMBER == 1:
        ACTIVE = False

print(sorted(list_prime_factors)[-1])
