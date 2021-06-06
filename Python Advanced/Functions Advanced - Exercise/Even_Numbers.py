def even_numbers(numbers):
    return [int(el) for el in numbers if int(el) % 2 == 0]


nums = input().split()
print(even_numbers(nums))
