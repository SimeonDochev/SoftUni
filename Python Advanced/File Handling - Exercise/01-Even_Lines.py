import re

with open('text.txt') as f:
    lines = f.readlines()

even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 0]

for line in even_lines:
    line = re.sub("[-,.!?]", '@', line)
    print(' '.join(line.split()[::-1]))
