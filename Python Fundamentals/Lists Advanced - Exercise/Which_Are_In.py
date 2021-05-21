substrings = input().split(", ")
words_list = input().split(", ")

filtered_words_list = [part for part in substrings for word in words_list if part in word]

print(sorted(set(filtered_words_list), key=filtered_words_list.index))
