command = input()

under_16 = 0
above_16 = 0
while command != 'Christmas':
    command = int(command)
    if command <= 16:
        under_16 += 1
    else:
        above_16 += 1
    command = input()

print(f'Number of adults: {above_16}')
print(f'Number of kids: {under_16}')
print(f'Money for toys: {under_16 * 5}')
print(f'Money for sweaters: {above_16 * 15}')
