factor = int(input())
count = int(input())

result = []
num = 1

while len(result) < count:
    if num % factor == 0:
        result.append(num)
    num += 1

print(result)