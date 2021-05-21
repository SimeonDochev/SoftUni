import sys

n = int(input())
max_even_number = -sys.maxsize
min_even_number = sys.maxsize
max_odd_number = -sys.maxsize
min_odd_number = sys.maxsize
odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num > max_even_number:
            max_even_number = num
        if num < min_even_number:
            min_even_number = num
    else:
        odd_sum += num
        if num > max_odd_number:
            max_odd_number = num
        if num < min_odd_number:
            min_odd_number = num

if even_sum == 0 and odd_sum == 0:
    print(f'OddSum={odd_sum:.2f},')
    print('OddMin=No,')
    print('OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print('EvenMin=No,')
    print('EvenMax=No')
elif even_sum == 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_odd_number:.2f},')
    print(f'OddMax={max_odd_number:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print('EvenMin=No,')
    print('EvenMax=No')
elif odd_sum == 0:
    print(f'OddSum={odd_sum:.2f},')
    print('OddMin=No,')
    print('OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={min_even_number:.2f},')
    print(f'EvenMax={max_even_number:.2f}')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_odd_number:.2f},')
    print(f'OddMax={max_odd_number:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={min_even_number:.2f},')
    print(f'EvenMax={max_even_number:.2f}')