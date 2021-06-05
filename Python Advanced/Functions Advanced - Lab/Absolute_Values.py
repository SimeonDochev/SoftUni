def absolute_values(nums):
    absolute_values = [abs(num) for num in nums]
    return absolute_values


nums = [float(num) for num in input().split()]
print(absolute_values(nums))
