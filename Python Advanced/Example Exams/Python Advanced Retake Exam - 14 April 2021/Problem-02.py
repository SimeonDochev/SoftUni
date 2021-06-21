from math import ceil
from collections import deque


def read_board():
    board = [[col for col in input().split()] for row in range(7)]

    return board


def validate_position(row, col):
    if 0 <= row < 7 and 0 <= col < 7:
        return True
    return False


def get_numbers_sum(row, col, board):
    nums = [
        int(board[row][0]),
        int(board[row][6]),
        int(board[0][col]),
        int(board[6][col]),
    ]

    return sum(nums)


first_player_name, second_player_name = input().split(', ')
points = {first_player_name: 501, second_player_name: 501}

throws = 1
players = deque([first_player_name, second_player_name])
board = read_board()

while True:
    current_player = players[0]
    pos_row, pos_col = eval(input())

    if validate_position(pos_row, pos_col):
        value = board[pos_row][pos_col]
        if value.isnumeric():
            points[current_player] -= int(value)
        elif value == "D":
            points[current_player] -= get_numbers_sum(pos_row, pos_col, board) * 2
        elif value == "T":
            points[current_player] -= get_numbers_sum(pos_row, pos_col, board) * 3
        elif value == "B":
            print(f"{current_player} won the game with {ceil(throws/2)} throws!")
            exit(0)

    if points[current_player] <= 0:
        print(f"{current_player} won the game with {ceil(throws/2)} throws!")
        exit(0)
    players.rotate()
    throws += 1
