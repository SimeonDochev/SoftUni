n = int(input())

longest_intersection = []

for _ in range(n):
    first_set = set()
    second_set = set()
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = [int(num) for num in first_range.split(",")]
    second_range_start, second_range_end = [int(num) for num in second_range.split(",")]
    for number in range(first_range_start, first_range_end+1):
        first_set.add(number)
    for number in range(second_range_start, second_range_end+1):
        second_set.add(number)
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
