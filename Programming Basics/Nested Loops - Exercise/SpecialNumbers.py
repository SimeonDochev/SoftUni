n = int(input())

for i in range(1111, 10000):
    counter = 0
    for digit in str(i):
        digit = int(digit)
        if digit != 0:
            if n % digit == 0:
                counter += 1
        else:
            continue
    if counter == 4:
        print(i, end=' ')
