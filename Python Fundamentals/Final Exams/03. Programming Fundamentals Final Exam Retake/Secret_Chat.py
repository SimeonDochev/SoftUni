concealed_message = input()

command = input()
while not command == "Reveal":
    command_data = command.split(":|:")
    action = command_data[0]
    if action == "InsertSpace":
        index = int(command_data[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    elif action == "Reverse":
        substring = command_data[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
        else:
            print("error")
            command = input()
            continue
    elif action == "ChangeAll":
        substring = command_data[1]
        replacement = command_data[2]
        concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")


