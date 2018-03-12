"""
problem:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

LIST_PALINDROME = []

#Search all the palindromes
for nb1 in range(100, 1000):
    for nb2 in range(100, 1000):
        k = list(str(nb1*nb2))

        #If k = reverse_k, it's a palindrome
        if k == [elt for elt in reversed(k)]:
            LIST_PALINDROME.append(int("".join(k)))

print(sorted(LIST_PALINDROME, reverse=True)[0])
