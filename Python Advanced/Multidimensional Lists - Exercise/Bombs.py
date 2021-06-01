def read_square_matrix():
    matrix = []
    rows_count = int(input())

    for row in range(rows_count):
        matrix.append([int(el) for el in input().split()])

    return matrix


def get_bombs_coordinates():
    raw_coordinates = input().split()
    bombs_coordinates = []
    for i in range(len(raw_coordinates)):
        current_coord = tuple(map(int, raw_coordinates[i].split(',')))
        bombs_coordinates.append(current_coord)

    return bombs_coordinates


def detonate_bomb(bomb_coordinates, matrix):
    row, col = bomb_coordinates
    bomb_value = matrix[row][col]
    cells_to_reduce = [(row, col), (row-1, col-1), (row-1, col), (row-1, col+1),
                       (row, col+1), (row+1, col+1), (row+1, col),
                       (row+1, col-1), (row, col-1)]
    if bomb_value > 0:
        for cell in cells_to_reduce:
            cell_row, cell_col = cell
            if 0 <= cell_row < len(matrix) and 0 <= cell_col < len(matrix):
                if not matrix[cell_row][cell_col] <= 0:
                    matrix[cell_row][cell_col] -= bomb_value


def find_alive_cells(matrix):
    alive_cells_positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if not matrix[row][col] <= 0:
                alive_cells_positions.append((row, col))

    return alive_cells_positions


def get_alive_cells_sum(matrix):
    alive_cells_sum = 0
    for cell in find_alive_cells(matrix):
        cell_row, cell_col = cell
        alive_cells_sum += matrix[cell_row][cell_col]

    return f"Sum: {alive_cells_sum}"


def main():
    matrix = read_square_matrix()

    all_bombs = get_bombs_coordinates()

    for i in range(len(all_bombs)):
        bomb_coordinates = all_bombs[i]
        detonate_bomb(bomb_coordinates, matrix)

    print(f"Alive cells: {len(find_alive_cells(matrix))}")
    print(get_alive_cells_sum(matrix))

    for row in range(len(matrix)):
        print(*matrix[row], sep=' ')


main()
