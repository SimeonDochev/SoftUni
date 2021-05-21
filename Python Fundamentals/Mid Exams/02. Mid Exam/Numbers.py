numbers_list = list(map(int, input().split()))

bigger_than_average = [num for num in numbers_list if num > sum(numbers_list) / len(numbers_list)]

if len(bigger_than_average) == 0:
    print("No")
elif 0 < len(bigger_than_average) <= 5:
    bigger_than_average.sort(reverse=True)
    bigger_than_average = list(map(str, bigger_than_average))
    print(' '.join(bigger_than_average))
else:
    for _ in range(5):
        print(max(bigger_than_average), end=' ')
        bigger_than_average.remove(max(bigger_than_average))
