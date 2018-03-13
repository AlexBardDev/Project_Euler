"""
problem: https://projecteuler.net/problem=14
"""

#Resol using the Collatz sequence

from operator import itemgetter

list_seq = []
list_n = [n for n in range(1, 1000000)]

for n in list_n:
    i = 1

    while True:
        i += 1
        q, r = divmod(n, 2)

        if r == 0:
            n = q
        else:
            n = (3*n)+1

        if n == 1:
            break

    list_seq.append(i)

print(sorted(zip(list_n, list_seq), key=itemgetter(1))[-1][0])
