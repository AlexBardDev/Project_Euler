"""
problem: https://projecteuler.net/problem=26
"""

from operator import itemgetter

list_cycles = []
list_info = []

for nb in range(2, 1000):
    result = list(str(1/nb)[2:])
    search = True
    while search:
        if len(result) > 1:
            d = result[0]
            if len(set(result)) == 1:
                list_cycles.append((nb, int(d)))
                search = False
            else:
                del result[0]
                if d in result:
                    sol = [d]
                    k = result.index(d)
                    i = 0
                    while (k+1+i) < len(result):
                        if result[i] == d:
                            break
                        elif result[i] == result[k+1+i]:
                            sol.append(result[i])
                            i += 1
                    list_cycles.append((nb, int("".join(sol))))
                    search = False
        else:
            search = False

print(sorted(list_cycles, key=itemgetter(1))[-1][0])
