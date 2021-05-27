n = int(input())

even_numbers_set = set()
odd_numbers_set = set()

line_counter = 1
for _ in range(n):
    name = input()
    current_sum = 0
    for char in name:
        current_sum += ord(char)
    current_sum //= line_counter
    line_counter += 1
    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)

if sum(even_numbers_set) == sum(odd_numbers_set):
    result = [int(num) for num in even_numbers_set | odd_numbers_set]
    print(*result, sep=", ")
elif sum(even_numbers_set) < sum(odd_numbers_set):
    result = [int(num) for num in odd_numbers_set - even_numbers_set]
    print(*result, sep=", ")
else:
    result = [int(num) for num in even_numbers_set ^ odd_numbers_set]
    print(*result, sep=", ")
