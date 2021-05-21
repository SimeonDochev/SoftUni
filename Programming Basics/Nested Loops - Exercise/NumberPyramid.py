n = int(input())

current = 1
is_bigger = False

for col in range(1, n+1):
    for row in range(1, col+1):
        if current > n:
            is_bigger = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_bigger:
        break
    print()
