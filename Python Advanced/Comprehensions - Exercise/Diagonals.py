n = int(input())

matrix = [[int(num) for num in input().split(', ')] for row in range(n)]

first_diagonal = []
second_diagonal = []

for row in range(n):
    for col in range(n):
        if row == col:
            first_diagonal.append(matrix[row][col])
        if row + col == n - 1:
            second_diagonal.append(matrix[row][col])

print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")
