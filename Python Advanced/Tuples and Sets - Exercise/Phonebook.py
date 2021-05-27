phonebook = {}

name_num = input()
while not name_num.isdigit():
    name, number = name_num.split("-")
    if name not in phonebook:
        phonebook[name] = None
    phonebook[name] = number
    name_num = input()

n = int(name_num)
for _ in range(n):
    name_to_find = input()
    if name_to_find not in phonebook:
        print(f"Contact {name_to_find} does not exist.")
    else:
        print(f"{name_to_find} -> {phonebook[name_to_find]}")
