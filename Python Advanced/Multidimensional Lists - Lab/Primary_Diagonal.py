n = int(input())

primary_diag_sum = 0

matrix = []
for row in range(n):
    matrix.append([int(num) for num in input().split()])
    primary_diag_sum += matrix[row][row]

print(primary_diag_sum)
