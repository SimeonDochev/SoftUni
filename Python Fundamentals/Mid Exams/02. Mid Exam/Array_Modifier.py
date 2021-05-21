def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def multiply(array, index1, index2):
    array[index1] *= array[index2]


def decrease(array):
    for num in range(len(array)):
        array[num] -= 1


numbers_list = list(map(int, input().split()))

command = input()
while not command == "end":
    if command == "decrease":
        decrease(numbers_list)
        command = input()
        continue
    action, index_1, index_2 = command.split()
    if action == "swap":
        swap(numbers_list, int(index_1), int(index_2))
    elif action == "multiply":
        multiply(numbers_list, int(index_1), int(index_2))
    command = input()

numbers_list = list(map(str, numbers_list))
print(', '.join(numbers_list))
