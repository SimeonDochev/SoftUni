import sys

n = int(input())
result = 0
biggest_number = -sys.maxsize

for i in range(n):
    num = int(input())
    if num > biggest_number:
        biggest_number = num
    result += num

other_sum = result - biggest_number

if biggest_number == other_sum:
    print('Yes')
    print(f'Sum = {biggest_number}')
else:
    print('No')
    print(f'Diff = {abs(biggest_number - other_sum)}')
