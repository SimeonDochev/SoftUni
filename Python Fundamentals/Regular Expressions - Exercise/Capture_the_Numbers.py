import re

text = input()
pattern = r"\d+"
numbers = []

while text:
    numbers.extend(re.findall(pattern, text))
    text = input()

print(*numbers)
