sequence = input()

stack = []

is_balanced = True

for paren in sequence:
    if paren in "([{":
        stack.append(paren)
    elif paren in ")]}":
        if len(stack) == 0:
            is_balanced = False
            break
        opening_paren = stack.pop()
        if f"{opening_paren}{paren}" not in ['[]', '()', '{}']:
            is_balanced = False
            break

if is_balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")