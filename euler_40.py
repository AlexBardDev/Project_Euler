"""
problem: https://projecteuler.net/problem=40
"""

fractional_part = ""
i = 1

while len(fractional_part) < 1000000:
    fractional_part += str(i)
    i += 1

k = 1
y = 9

while len(fractional_part) >= y:
    k *= (int(fractional_part[y]))
    y = int(str(y) + "9")

print(k)
