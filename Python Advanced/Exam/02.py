def create_field():
    field = [[col for col in input().split()] for row in range(5)]

    return field


def get_coordinates(field):
    player_position = None
    targets = []
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == "A":
                player_position = (row, col)
            elif field[row][col] == "x":
                targets.append((row, col))
    return player_position, targets


def validate_next_pos(field, player_position, direction, steps):
    cur_row, cur_col = player_position
    if direction == "right":
        if cur_col + steps < len(field) and field[cur_row][cur_col+steps] == ".":
            return True
    elif direction == "left":
        if cur_col - steps >= 0 and field[cur_row][cur_col - steps] == ".":
            return True
    elif direction == "up":
        if cur_row - steps >= 0 and field[cur_row - steps][cur_col] == ".":
            return True
    elif direction == "down":
        if cur_row + steps < len(field) and field[cur_row + steps][cur_col] == ".":
            return True

    return False


field = create_field()
player_pos, targets = get_coordinates(field)

total_targets = len(targets)
targets_hit_count = 0
targets_hit_coordinates = []

commands_count = int(input())

for _ in range(commands_count):
    command_data = input().split()
    current_cmd = command_data[0]
    direction = command_data[1]
    if current_cmd == "move":
        row, col = player_pos
        steps = int(command_data[2])
        if validate_next_pos(field, player_pos, direction, steps):
            field[row][col] = '.'
            if direction == "up":
                field[row-steps][col] = 'A'
                player_pos = (row-steps, col)
            elif direction == "down":
                field[row+steps][col] = 'A'
                player_pos = (row+steps, col)
            elif direction == "right":
                field[row][col+steps] = 'A'
                player_pos = (row, col+steps)
            elif direction == "left":
                field[row][col-steps] = 'A'
                player_pos = (row, col-steps)
    elif current_cmd == "shoot":
        row, col = player_pos
        if direction == "up":
            for idx in range(1, 6):
                if row - idx >= 0:
                    if field[row-idx][col] == "x":
                        targets_hit_count += 1
                        targets_hit_coordinates.append([row-idx, col])
                        field[row-idx][col] = "."
                        targets.remove((row-idx, col))
                        break
                else:
                    break
        elif direction == "down":
            for idx in range(1, 6):
                if row + idx < len(field):
                    if field[row+idx][col] == "x":
                        targets_hit_count += 1
                        targets_hit_coordinates.append([row+idx, col])
                        field[row+idx][col] = "."
                        targets.remove((row+idx, col))
                        break
                else:
                    break
        elif direction == "right":
            for idx in range(1, 6):
                if col + idx < len(field):
                    if field[row][col+idx] == "x":
                        targets_hit_count += 1
                        targets_hit_coordinates.append([row, col+idx])
                        field[row][col+idx] = "."
                        targets.remove((row, col+idx))
                        break
                else:
                    break
        elif direction == "left":
            for idx in range(1, 6):
                if col - idx >= 0:
                    if field[row][col - idx] == "x":
                        targets_hit_count += 1
                        targets_hit_coordinates.append([row, col - idx])
                        field[row][col - idx] = "."
                        targets.remove((row, col - idx))
                        break
                else:
                    break
    if not targets:
        break

if not targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {len(targets)} targets left.")

if targets_hit_coordinates:
    for coord in targets_hit_coordinates:
        print(coord)
