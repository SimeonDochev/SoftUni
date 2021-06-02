n = int(input())

even_matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for row in range(n)]

print(even_matrix)
