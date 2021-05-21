nums_list = list(map(lambda x: int(x), input().split(", ")))

group = 10

while nums_list:
    current_group = []
    for num in nums_list:
        if num <= group:
            current_group.append(num)
    for num in current_group:
        nums_list.remove(num)

    print(f"Group of {group}'s: {current_group}")
    group += 10
