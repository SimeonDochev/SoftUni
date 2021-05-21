n = int(input())

p1 = 0
p2 = 0
p3 = 0
total_count = 0

for i in range(n):
    num = int(input())
    total_count += 1
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

print(f'{p1 / total_count * 100:.2f}%')
print(f'{p2 / total_count * 100:.2f}%')
print(f'{p3 / total_count * 100:.2f}%')
