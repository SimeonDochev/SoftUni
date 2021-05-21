numbers = input()
beggars = int(input())

numbers_list = numbers.split(", ")

result = []
beggar_turn = 0

for beggar in range(beggars):
    current_beggar_sum = 0
    for num in range(beggar_turn, len(numbers_list), beggars):
        current_beggar_sum += int(numbers_list[num])
    result.append(current_beggar_sum)
    beggar_turn += 1

print(result)
