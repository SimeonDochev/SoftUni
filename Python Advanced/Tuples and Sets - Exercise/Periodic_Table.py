n = int(input())

unique_elements = set()

for _ in range(n):
    [unique_elements.add(el) for el in input().split()]

print('\n'.join(unique_elements))
