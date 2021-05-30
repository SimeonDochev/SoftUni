n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(num) for num in input().split()])

primary_dia_sum = 0
secondary_dia_sum = 0

for row in range(n):
    for col in range(n):
        if row == col:
            primary_dia_sum += matrix[row][row]
        if row + col == n - 1:
            secondary_dia_sum += matrix[row][col]

print(abs(primary_dia_sum - secondary_dia_sum))

