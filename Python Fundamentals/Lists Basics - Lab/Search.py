n = int(input())
searched_word = input()

full_list = []
filtered_list = []

for _ in range(n):
    given_string = input()
    full_list.append(given_string)
    if searched_word in given_string:
        filtered_list.append(given_string)

print(full_list)
print(filtered_list)