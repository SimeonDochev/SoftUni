usernames = input().split(", ")

for username in usernames:
    is_valid = True
    if not 3 <= len(username) <= 16:
        is_valid = False

    if is_valid:
        for char in username:
            if not char.isalpha() and not char.isdigit() and not char == "_" and not char == "-":
                is_valid = False
                break
    if is_valid:
        print(username)
