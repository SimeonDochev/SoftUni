n = int(input())

positive_nums = []
negative_nums = []

for _ in range(n):
    num = int(input())
    if num < 0:
        negative_nums.append(num)
    else:
        positive_nums.append(num)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}")
