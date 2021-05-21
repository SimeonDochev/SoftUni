text = input().split(">")

result = []
explosion = 0

for el in text:
    if el[0].isdigit():
        explosion += int(el[0])
        if len(el) <= explosion:
            explosion -= len(el)
            el = ">"
        else:
            el = ">" + el[explosion::]
            explosion = 0
    result.append(el)

print(''.join(result))
