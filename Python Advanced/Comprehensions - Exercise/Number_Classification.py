numbers = input()

print(f"Positive: {', '.join([num for num in numbers.split(', ') if int(num) >= 0])}")
print(f"Negative: {', '.join([num for num in numbers.split(', ') if int(num) < 0])}")
print(f"Even: {', '.join([num for num in numbers.split(', ') if int(num) % 2 == 0])}")
print(f"Odd: {', '.join([num for num in numbers.split(', ') if not int(num) % 2 == 0])}")
