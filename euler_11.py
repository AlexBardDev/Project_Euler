"""
problem: https://projecteuler.net/problem=11
"""

list_lines = []
result = 0

for i in range(20):
    line = [int(elt) for elt in input("""> """).split()]
    list_lines.append(line)

#Left to right
for line in list_lines:
    for i, elt in enumerate(line):
        if (i+3) < 20:
            product = elt*line[i+1]*line[i+2]*line[i+3]
            if product > result:
                result = product
        else:
            break

#Up to down
for i, line in enumerate(list_lines):
    for j, elt in enumerate(line):
        if (i+3) < 20:
            product = elt*list_lines[i+1][j]*list_lines[i+2][j]*list_lines[i+3][j]
            if product > result:
                result = product

#Diagonal: up-left to down-right
for i, line in enumerate(list_lines):
    for j, elt in enumerate(line):
        if (i+3) < 20 and (j+3) < 20:
            product = elt*list_lines[i+1][j+1]*list_lines[i+2][j+2]*list_lines[i+3][j+3]
            if product > result:
                result = product

#Diagonal: down-left to up-right
def generator(my_list):
    """My generator to use the for loop in the opposite way"""

    n = 1
    k = len(my_list)
    while (k-n) >= 0:
        yield (k-n), my_list[k-n]
        n += 1

for i, line in generator(list_lines):
    for j, elt in enumerate(line):
        if (i-3) >= 0 and (j+3) < 20:
            product = elt*list_lines[i-1][j+1]*list_lines[i-2][j+2]*list_lines[i-3][j+3]
            if product > result:
                result = product

print(result)
