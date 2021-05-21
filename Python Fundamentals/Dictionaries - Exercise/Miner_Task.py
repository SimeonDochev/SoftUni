resources = {}

command = input()
while not command == "stop":
    resource = command
    quantity = int(input())
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity
    command = input()

for r, q in resources.items():
    print(f"{r} -> {q}")
