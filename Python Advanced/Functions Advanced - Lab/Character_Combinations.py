from itertools import permutations

chars = input()
result = list(permutations(chars, len(chars)))

for combination in result:
    print(*combination, sep='')
