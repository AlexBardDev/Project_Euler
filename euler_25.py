"""
problem: https://projecteuler.net/problem=25
"""

list_fibonacci = [1, 1]

while True:
    list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2])

    if len(str(list_fibonacci[-1])) >= 1000:
        break

print(len(list_fibonacci))
