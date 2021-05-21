text = input().split()

sums = []

for token in text:
    current_sum = 0
    first_letter = token[0]
    second_letter = token[-1]
    number = int(token[1:-1])
    if first_letter.isupper():
        current_sum += number / (ord(first_letter)-64)
    else:
        current_sum += number * (ord(first_letter)-96)

    if second_letter.isupper():
        current_sum -= (ord(second_letter)-64)
    else:
        current_sum += (ord(second_letter)-96)
    sums.append(current_sum)

total_sum = sum(sums)
print(f"{total_sum:.2f}")
