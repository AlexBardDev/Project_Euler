"""
problem: https://projecteuler.net/problem=8
"""

list_digit = [int(elt) for elt in list(input("> "))]

list_solution = [0]

product = 1

for i, elt in enumerate(list_digit) :
    if i < len(list_digit)-12 :
        for nbre in range(1, 13) :
            product *= list_digit[i+nbre]
        product *= elt
        if product > list_solution[0] :
            list_solution.insert(0, product)
            product = 1
        else :
            product = 1

print(list_solution[0])
