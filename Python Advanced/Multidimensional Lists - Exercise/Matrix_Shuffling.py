rows, cols = [int(num) for num in input().split()]

matrix = []
for row in range(rows):
    matrix.append(input().split())

command = input()
while not command == "END":
    try:
        command_data = command.split()
        if not command_data[0] == "swap":
            print("Invalid input!")
            command = input()
            continue
        r1, c1, r2, c2 = int(command_data[1]), int(command_data[2]), int(command_data[3]), int(command_data[4])
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        for row in matrix:
            print(*row, sep=' ')
        command = input()
    except:
        print("Invalid input!")
        command = input()
