interval1 = int(input())
interval2 = int(input())
magic_number = int(input())
counter = 0
is_found = False

for i in range(interval1, interval2+1):
    for j in range(interval1, interval2+1):
        counter += 1
        if i + j == magic_number:
            is_found = True
            print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
            break
    if is_found == True:
        break
if not is_found:
    print(f'{counter} combinations - neither equals {magic_number}')
