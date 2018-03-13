"""
problem: https://projecteuler.net/problem=22
"""

import requests

req = requests.get("https://projecteuler.net/project/resources/p022_names.txt")

print(sum([sum([ord(letter)-64 for letter in prenom if letter != "\""])*(i+1)
           for i, prenom in enumerate(sorted(req.text.split(",")))]))
