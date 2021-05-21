text = list(input())

stack = []

while text:
    stack.append(text.pop())

print(f"{''.join(stack)}")
