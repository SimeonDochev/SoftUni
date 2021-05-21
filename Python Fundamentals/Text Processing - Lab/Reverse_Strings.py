command = input()

while not command == "end":
    word = command
    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")
    command = input()
