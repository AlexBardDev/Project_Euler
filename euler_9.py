"""
problem: https://projecteuler.net/problem=9
"""

a = 1
b = 2

while True:
    if a+b-((a*b)/1000) == 500:
        break
    elif b < 997:
        b += 1
    else:
        a += 1
        b = (a+1)

c = 1000 - (a+b)

print((a*b*c))
