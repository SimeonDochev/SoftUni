from sys import maxsize

rows, cols = [int(num) for num in input().split()]

matrix = []
for row in range(rows):
    matrix.append([int(num) for num in input().split()])

biggest_sum = -maxsize
position = None
for row in range(rows-2):
    for col in range(cols-2):
        current_sum = 0
        for sub_row in range(3):
            for sub_col in range(3):
                current_sum += matrix[row+sub_row][col+sub_col]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            position = row, col

if position:
    print(f"Sum = {biggest_sum}")
    row, col = position
    print(matrix[row][col], matrix[row][col+1], matrix[row][col+2])
    print(matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2])
    print(matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2])
