rows, cols = [int(num) for num in input().split(", ")]

matrix = []
total_sum = 0

for row in range(rows):
    matrix.append(list(int(num) for num in input().split(", ")))
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)
