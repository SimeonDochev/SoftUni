import re

text = input()
pattern = r"(@|#)(?P<pair>[a-zA-Z]{3,}\1\1[a-zA-Z]{3,})\1"

pairs = [obj.group('pair') for obj in re.finditer(pattern, text)]
valid_pairs = []

for pair in pairs:
    half = int(len(pair)/2)
    first_word = pair[:half-1]
    second_word = pair[half+1:]
    if first_word == second_word[::-1]:
        valid_pairs.append(first_word + " <=> " + second_word)

if not pairs:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(pairs)} word pairs found!")
    if valid_pairs:
        print("The mirror words are:")
        print(*valid_pairs, sep=', ')
    else:
        print("No mirror words!")
