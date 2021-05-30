n = int(input())

primary_dia_sum = 0

matrix = []
for row in range(n):
    matrix.append([int(num) for num in input().split()])
    primary_dia_sum += matrix[row][row]

print(primary_dia_sum)
