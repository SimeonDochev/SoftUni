width = int(input())
length = int(input())
size = width * length
total_pieces = 0

while True:
    command = input()
    if command == 'STOP':
        print(f'{size - total_pieces} pieces are left.')
        break
    command = int(command)
    total_pieces += command
    if total_pieces > size:
        print(f'No more cake left! You need {total_pieces - size} pieces more.')
        break
