def valid_coordinates(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


rows = int(input())

matrix = [[int(el) for el in input().split()]for row in range(rows)]

command = input()
while not command == "END":
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if valid_coordinates(row, col):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

for row in matrix:
    print(*row)
