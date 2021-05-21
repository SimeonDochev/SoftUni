import re

text = input()
emoji_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
digits_pattern = r"\d"
cool_threshold = 1

digits_list = [int(digit) for digit in re.findall(digits_pattern, text)]

for digit in digits_list:
    cool_threshold *= digit
print(f"Cool threshold: {cool_threshold}")

emojis = [obj.group() for obj in re.finditer(emoji_pattern, text)]
cool_emojis = []

for emoji in emojis:
    coolness = 0
    for char in emoji:
        if char.isalpha():
            coolness += ord(char)
    if coolness >= cool_threshold:
        cool_emojis.append(emoji)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
