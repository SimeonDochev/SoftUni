text = input()

message = ""
current = ""

for i in range(len(text)):
    if not text[i].isdigit():
        current += text[i]
    else:
        if i == len(text) - 1:
            message += current.upper() * int(text[i])
        else:
            if text[i+1].isdigit():
                rep = int(text[i]+text[i+1])
                message += current.upper()*rep
                current = ""
            else:
                message += current.upper() * int(text[i])
                current = ""

unique_symbols = ""
for sym in message:
    if sym.lower() not in unique_symbols:
        unique_symbols += sym.lower()

print(f"Unique symbols used: {len(unique_symbols)}")
print(message)
