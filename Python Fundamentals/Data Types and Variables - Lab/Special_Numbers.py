n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    num_as_string = str(num)
    for digit in num_as_string:
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
