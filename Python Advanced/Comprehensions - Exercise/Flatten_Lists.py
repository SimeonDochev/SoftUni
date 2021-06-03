numbers = input().split("|")

numbers = numbers[::-1]

result = [num.strip() for i in range(len(numbers)) for num in numbers[i].split()]

print(*result)
