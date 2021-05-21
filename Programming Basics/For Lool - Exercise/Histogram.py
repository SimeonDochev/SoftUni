n = int(input())
total_count = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    total_count += 1
    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / total_count * 100:.2f}%')
print(f'{p2 / total_count * 100:.2f}%')
print(f'{p3 / total_count * 100:.2f}%')
print(f'{p4 / total_count * 100:.2f}%')
print(f'{p5 / total_count * 100:.2f}%')
