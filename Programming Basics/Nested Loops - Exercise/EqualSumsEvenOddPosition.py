n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    counter = 1
    even_sum = 0
    odd_sum = 0
    for digit in str(i):
        if counter % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
        counter += 1
    if even_sum == odd_sum:
        print(i, end=' ')
