capacity = float(input())

counter = 0
suitcases_loaded = 0
command = input()
while command != 'End':
    counter += 1
    if counter % 3 == 0:
        capacity -= float(command) * 1.1
    else:
        capacity -= float(command)
    if capacity < 0:
        print('No more space!')
        break
    suitcases_loaded += 1
    command = input()

if command == 'End':
    print('Congratulations! All suitcases are loaded!')
print(f'Statistic: {suitcases_loaded} suitcases loaded.')