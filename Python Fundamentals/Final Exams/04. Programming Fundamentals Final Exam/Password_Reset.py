password = input()

command = input()
while not command == "Done":
    command_data = command.split()
    action = command_data[0]
    if action == "TakeOdd":
        new_pass = ""
        for i in range(1, len(password), 2):
            new_pass += password[i]
        password = new_pass
        print(password)
    elif action == "Cut":
        index = int(command_data[1])
        length = int(command_data[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif action == "Substitute":
        substring = command_data[1]
        substitute = command_data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
