text = input()

new_text = ""
last_added_char = ""

for i in range(len(text)):
    if text.count(text[i]) == 1:
        new_text += text[i]
        last_added_char = text[i]
        continue
    if not text[i] == last_added_char:
        new_text += text[i]
        last_added_char = text[i]

print(new_text)
