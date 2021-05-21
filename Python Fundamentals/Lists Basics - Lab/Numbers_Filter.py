n = int(input())

even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
    if num < 0:
        negative_nums.append(num)
    else:
        positive_nums.append(num)

command = input()

if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "negative":
    print(negative_nums)
else:
    print(positive_nums)
