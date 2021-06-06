def negative_vs_positive(numbers):
    positive_nums = sum(filter(lambda x: x > 0, numbers))
    negative_nums = sum(filter(lambda x: x < 0, numbers))
    print(negative_nums)
    print(positive_nums)
    if abs(negative_nums) < positive_nums:
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(el) for el in input().split()]
negative_vs_positive(nums)
