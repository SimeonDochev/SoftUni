numbers = tuple([float(num) for num in input().split()])

result = {}

for num in numbers:
    if num not in result:
        result[num] = numbers.count(num)

for num in result:
    print(f"{num} - {result[num]} times")
