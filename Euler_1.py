sum_multiples = 0 

for nb in range(1,1000):
    if nb%3 == 0:
        sum_multiples += nb
    elif nb%5 == 0:
        sum_multiples += nb

print(sum_multiples)
