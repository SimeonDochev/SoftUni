def min_max_and_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)


nums = [int(el) for el in input().split()]
min_num, max_num, nums_sum = min_max_and_sum(nums)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {nums_sum}")
