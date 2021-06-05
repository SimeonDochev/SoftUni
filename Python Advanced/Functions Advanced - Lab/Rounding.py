def round_numbers(nums):
    round_values = [round(num) for num in nums]
    return round_values


nums = [float(num) for num in input().split()]
print(round_numbers(nums))
