list_of_strings = input().split()

for word in list_of_strings:
    print(word * len(word), end="")
