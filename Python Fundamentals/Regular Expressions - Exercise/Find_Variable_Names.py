import re

text = input()
pattern = r"(?<=\s_)[A-Za-z0-9]+\b"

variables = [obj.group() for obj in re.finditer(pattern, text)]

print(*variables, sep=',')
