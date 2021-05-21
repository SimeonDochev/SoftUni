email = input()

command = input()
while not command == "Complete":
    command = command.rstrip()
    if command == "Make Upper":
        email = email.upper()
        print(email.rstrip())
    elif command == "Make Lower":
        email = email.lower()
        print(email.rstrip())
    elif command == "GetUsername":
        username = ""
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            for char in email:
                if not char == "@":
                    username += char
                else:
                    break
            print(username.rstrip())
    elif command == "Encrypt":
        for char in email:
            print(ord(char), end=" ")
        print()
    else:
        command_data = command.split()
        action = command_data[0]
        if action == "GetDomain":
            count = int(command_data[1])
            domain = email.rstrip()[-count:]
            print(domain)
        elif action == "Replace":
            char = command_data[1]
            email = email.replace(char, "-")
            print(email.rstrip())
    command = input()

