n = int(input())

stack = []

for q in range(n):
    query = input()
    if query.startswith("1"):
        element = int(query.split()[-1])
        stack.append(element)
    else:
        if stack:
            if query.startswith("2"):
                stack.pop()
            elif query.startswith("3"):
                print(max(stack))
            elif query.startswith("4"):
                print(min(stack))

result = []
while stack:
    result.append(stack.pop())

result = list(map(str, result))
print(', '.join(result))
