command = input()

total_sum = 0
while command != 'NoMoreMoney':
    command = float(command)
    if command < 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {command:.2f}')
    total_sum += command
    command = input()

print(f'Total: {total_sum:.2f}')
