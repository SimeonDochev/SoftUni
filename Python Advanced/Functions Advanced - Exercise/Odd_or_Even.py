def odd_or_even_numbers_sum(command, numbers):
    if command == "Odd":
        odd_numbers_sum = sum(filter(lambda x: not x % 2 == 0, numbers))
        return odd_numbers_sum
    even_numbers_sum = sum(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers_sum


command = input()
nums = [int(el) for el in input().split()]

print(odd_or_even_numbers_sum(command, nums) * len(nums))
