n = int(input())

matrix = []
for row in range(n):
    matrix.append(list(input()))

knights_removed = 0
while True:
    if n < 3:
        print(0)
        break
    max_danger = 0
    max_danger_position = None
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                current_danger = 0
                for i in range(8):
                    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
                    cols = [-1, -2, -2, -1, 1, 2, 2, 1]
                    if 0 <= row+rows[i] < n and 0 <= col+cols[i] < n:
                        if matrix[row+rows[i]][col+cols[i]] == "K":
                            current_danger += 1
                if current_danger > max_danger:
                    max_danger = current_danger
                    max_danger_position = row, col
    if max_danger:
        row, col = max_danger_position
        matrix[row][col] = "0"
        knights_removed += 1
    else:
        break

if knights_removed:
    print(knights_removed)
