"""
problem: https://projecteuler.net/problem=28
"""

list_nb = [elt for elt in range(1, (1001**2)+1)]
list_nb_diagonal = []

i = 0
list_nb_diagonal.append(list_nb[i])

k = 0
d = 2
i += d
while i < len(list_nb):
    list_nb_diagonal.append(list_nb[i])
    k += 1
    if k == 4:
        k = 0
        d += 2
    i += d

print(sum(list_nb_diagonal))
