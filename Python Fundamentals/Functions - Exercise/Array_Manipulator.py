from sys import maxsize


def exchange_after_index(array, index):
    first_half = array[:index+1]
    second_half = array[index+1:]
    new_array = second_half + first_half
    return new_array


def index_of_max_even_or_odd(array, even_or_odd):
    max_even = -maxsize
    max_odd = -maxsize
    if even_or_odd == "even":
        for el in range(len(array)):
            if array[el] % 2 == 0 and array[el] > max_even:
                max_even = array[el]
        if max_even == -maxsize:
            return "No matches"
        if array.count(max_even) == 1:
            return array.index(max_even)
        else:
            return len(array) - array[::-1].index(max_even) - 1
    elif even_or_odd == "odd":
        for el in range(len(array)):
            if not array[el] % 2 == 0 and array[el] > max_odd:
                max_odd = array[el]
        if max_odd == -maxsize:
            return "No matches"
        if array.count(max_odd) == 1:
            return array.index(max_odd)
        else:
            return len(array) - array[::-1].index(max_odd) - 1


def index_of_min_even_or_odd(array, even_or_odd):
    min_even = maxsize
    min_odd = maxsize
    if even_or_odd == "even":
        for el in range(len(array)):
            if array[el] % 2 == 0 and array[el] < min_even:
                min_even = array[el]
        if min_even == maxsize:
            return "No matches"
        if array.count(min_even) == 1:
            return array.index(min_even)
        else:
            return len(array) - array[::-1].index(min_even) - 1
    elif even_or_odd == "odd":
        for el in range(len(array)):
            if not array[el] % 2 == 0 and array[el] < min_odd:
                min_odd = array[el]
        if min_odd == maxsize:
            return "No matches"
        if array.count(min_odd) == 1:
            return array.index(min_odd)
        else:
            return len(array) - array[::-1].index(min_odd) - 1


def first_even_or_odd_elements(array, count, even_or_odd):
    filtered_numbers = []
    if even_or_odd == "even":
        for el in range(len(array)):
            if array[el] % 2 == 0:
                filtered_numbers.append(array[el])
    elif even_or_odd == "odd":
        for el in range(len(array)):
            if not array[el] % 2 == 0:
                filtered_numbers.append(array[el])
    return filtered_numbers[0:count]


def last_even_or_odd_elements(array, count, even_or_odd):
    filtered_numbers = []
    if even_or_odd == "even":
        for el in range(len(array)):
            if array[el] % 2 == 0:
                filtered_numbers.append(array[el])
    elif even_or_odd == "odd":
        for el in range(len(array)):
            if not array[el] % 2 == 0:
                filtered_numbers.append(array[el])
    return filtered_numbers[-count:]


array_from_console = input().split()
map_object = map(int, array_from_console)
array_as_integers = list(map_object)

command = input()
while not command == "end":
    new_command = command.split()
    if new_command[0] == "exchange":
        i = int(new_command[1])
        if i < 0 or i > len(array_as_integers)-1:
            print("Invalid index")
        else:
            array_as_integers = exchange_after_index(array_as_integers, i)
    elif new_command[0] == "max":
        even_or_odd_command = new_command[1]
        print(index_of_max_even_or_odd(array_as_integers, even_or_odd_command))
    elif new_command[0] == "min":
        even_or_odd_command = new_command[1]
        print(index_of_min_even_or_odd(array_as_integers, even_or_odd_command))
    elif new_command[0] == "first":
        elements_count = int(new_command[1])
        even_or_odd_command = new_command[2]
        if elements_count > len(array_as_integers):
            print("Invalid count")
        else:
            print(first_even_or_odd_elements(array_as_integers, elements_count, even_or_odd_command))
    elif new_command[0] == "last":
        elements_count = int(new_command[1])
        even_or_odd_command = new_command[2]
        if elements_count > len(array_as_integers):
            print("Invalid count")
        else:
            print(last_even_or_odd_elements(array_as_integers, elements_count, even_or_odd_command))

    command = input()

print(array_as_integers)
