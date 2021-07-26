def reverse_text(text):
    start_idx = len(text) - 1
    end_idx = 0
    while start_idx >= end_idx:
        yield text[start_idx]
        start_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
