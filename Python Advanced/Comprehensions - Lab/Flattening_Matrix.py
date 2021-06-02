n = int(input())

flattened_matrix = []

for _ in range(n):
    flattened_matrix.extend([int(el) for el in input().split(', ')])

print(flattened_matrix)
