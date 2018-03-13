"""
problem: https://projecteuler.net/problem=18

The resolving process is exactly the same for
the problem number 67 : https://projecteuler.net/problem=67
"""

list_lines = [[int(elt) for elt in input("> ").split()] for i in range(100)]

while list_lines[-2] != list_lines[0]:
    adline = list_lines[-2]
    dline = list_lines[-1]
    for i, elt in enumerate(adline):
        if dline[i] > dline[i+1]:
            list_lines[-2][i] += dline[i]
        else:
            list_lines[-2][i] += dline[i+1]
    del list_lines[-1]

print(list_lines[0][0] + max(list_lines[1]))
