list_of_numbers = input().split()
removed_numbers_amount = int(input())

map_object = map(int, list_of_numbers)
list_of_integers = list(map_object)

for _ in range(removed_numbers_amount):
    smallest_num = min(list_of_integers)
    list_of_integers.remove(smallest_num)

print(list_of_integers)
