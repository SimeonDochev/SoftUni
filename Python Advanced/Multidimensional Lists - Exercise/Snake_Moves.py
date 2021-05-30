from collections import deque

rows, cols = [int(num) for num in input().split()]
snake = deque(input())

matrix = []

for row in range(1, rows+1):
    current_row = []
    for col in range(cols):
        current_row.append(snake[0])
        snake.rotate(-1)
    if row % 2 == 0:
        current_row = current_row[::-1]
    matrix.append(current_row)

for row in matrix:
    print(*row, sep='')
