"""
problem: https://projecteuler.net/problem=29
"""

list_nb = []

for a in range(2, 101):
    for b in range(2, 101):
        list_nb.append(a**b)

print(len(list(set(list_nb))))
