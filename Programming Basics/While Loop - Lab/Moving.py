width = int(input())
length = int(input())
height = int(input())
command = input()
space = width * length * height
taken_space = 0

while command != 'Done':
    command = int(command)
    taken_space += command
    if taken_space > space:
        print(f'No more free space! You need {abs(space-taken_space)} Cubic meters more.')
        break
    command = input()

if space > taken_space:
    print(f'{space - taken_space} Cubic meters left.')