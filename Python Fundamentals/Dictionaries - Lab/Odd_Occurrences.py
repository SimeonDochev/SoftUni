words = input().split()

words_occurrences = {}

for word in words:
    current_word = word.lower()
    if current_word not in words_occurrences:
        words_occurrences[current_word] = 0
    words_occurrences[current_word] += 1

for word, occurrence in words_occurrences.items():
    if not occurrence % 2 == 0:
        print(word, end=" ")
