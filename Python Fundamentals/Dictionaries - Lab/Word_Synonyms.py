n = int(input())

synonyms_dict = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = [synonym]
    else:
        synonyms_dict[word].append(synonym)

for word, synonyms in synonyms_dict.items():
    print(f"{word} - {', '.join(synonyms)}")
