from collections import deque


def create_field(size):
    field = [[col for col in input().split()] for row in range(size)]

    return field


def find_coordinates(field):
    start_position = None
    end_position = None
    coal_coordinates = []
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == "s":
                start_position = (row, col)
            elif field[row][col] == "e":
                end_position = (row, col)
            elif field[row][col] == "c":
                coal_coordinates.append((row, col))

    return start_position, end_position, coal_coordinates


def validate_next_position(current_position, direction, field):
    curr_row, curr_col = current_position
    if direction == "left":
        if curr_col - 1 >= 0:
            return True
    elif direction == "right":
        if curr_col + 1 < len(field):
            return True
    elif direction == "up":
        if curr_row - 1 >= 0:
            return True
    elif direction == "down":
        if curr_row + 1 < len(field):
            return True

    return False


def main():
    field_size = int(input())
    commands = deque(cmd for cmd in input().split())

    field = create_field(field_size)
    start_position, end_position, coal_coordinates = find_coordinates(field)
    game_over = False

    current_position = start_position

    while commands:
        current_command = commands.popleft()
        row, col = current_position
        if validate_next_position(current_position, current_command, field):
            if current_command == "left":
                row, col = row, col - 1
                if (row, col) in coal_coordinates:
                    coal_coordinates.remove((row, col))
                    field[row][col] = "*"
                elif (row, col) == end_position:
                    print(f"Game over! ({row}, {col})")
                    game_over = True
                    break
            elif current_command == "right":
                row, col = row, col + 1
                if (row, col) in coal_coordinates:
                    coal_coordinates.remove((row, col))
                    field[row][col] = "*"
                elif (row, col) == end_position:
                    print(f"Game over! ({row}, {col})")
                    game_over = True
                    break
            elif current_command == "up":
                row, col = row - 1, col
                if (row, col) in coal_coordinates:
                    coal_coordinates.remove((row, col))
                    field[row][col] = "*"
                elif (row, col) == end_position:
                    print(f"Game over! ({row}, {col})")
                    game_over = True
                    break
            elif current_command == "down":
                row, col = row + 1, col
                if (row, col) in coal_coordinates:
                    coal_coordinates.remove((row, col))
                    field[row][col] = "*"
                elif (row, col) == end_position:
                    print(f"Game over! ({row}, {col})")
                    game_over = True
                    break
        else:
            continue

        current_position = row, col
        if not coal_coordinates:
            print(f"You collected all coals! ({row}, {col})")
            break

    row, col = current_position
    if coal_coordinates and not game_over:
        print(f"{len(coal_coordinates)} coals left. ({row}, {col})")


main()
