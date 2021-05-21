activation_key = input()

command = input()
while not command == "Generate":
    command_data = command.split(">>>")
    instruction = command_data[0]
    if instruction == "Contains":
        substring = command_data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instruction == "Flip":
        case = command_data[1]
        start_index = int(command_data[2])
        end_index = int(command_data[3])
        substring = activation_key[start_index:end_index]
        if case == "Upper":
            activation_key = activation_key.replace(substring, substring.upper())
        else:
            activation_key = activation_key.replace(substring, substring.lower())
        print(activation_key)
    elif instruction == "Slice":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")
