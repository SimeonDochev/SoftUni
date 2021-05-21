char_count = int(input())

result = 0

for i in range(char_count):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")
