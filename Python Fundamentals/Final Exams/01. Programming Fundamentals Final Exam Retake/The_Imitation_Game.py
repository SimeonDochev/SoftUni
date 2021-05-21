def move(string, number_of_letters):
    new_string = string[number_of_letters:] + string[:number_of_letters]
    return new_string


def insert(string, index, value):
    new_string = string[:index] + value + string[index:]
    return new_string


def change_all(string, substring, replacement):
    new_string = string.replace(substring, replacement)
    return new_string


encrypted_message = input()

command = input()
while not command == "Decode":
    command_data = command.split("|")
    if command_data[0] == "Move":
        number_of_letters = int(command_data[1])
        encrypted_message = move(encrypted_message, number_of_letters)
    elif command_data[0] == "Insert":
        index = int(command_data[1])
        value = command_data[2]
        encrypted_message = insert(encrypted_message, index, value)
    elif command_data[0] == "ChangeAll":
        substring = command_data[1]
        replacement = command_data[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")
