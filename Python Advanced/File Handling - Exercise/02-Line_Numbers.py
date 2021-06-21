with open('text.txt') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for i, line in enumerate(lines):
        line = line.strip()
        letters_count = len([char for char in line if char.isalpha()])
        punctuation_count = len([char for char in line if char in r'!\',.?-'])
        f.write(f"Line {i+1}: {line} ({letters_count})({punctuation_count})\n")
