numbers = input().split()

stack = []

while numbers:
    stack.append(numbers.pop())

print(' '.join(stack))
