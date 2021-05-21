string = input()

chars = {}

for char in string:
    if char == " ":
        continue
    if char not in chars:
        chars[char] = 0
    chars[char] += 1

for char, count in chars.items():
    print(f"{char} -> {count}")
