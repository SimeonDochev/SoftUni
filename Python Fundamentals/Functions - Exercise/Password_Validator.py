def password_validator(password):
    fulfilled = True
    if len(password) < 6 or len(password) > 10:
        fulfilled = False
        print("Password must be between 6 and 10 characters")
    digits_count = 0
    special_characters = False
    for char in password:
        if char.isdigit():
            digits_count += 1
        if not char.isdigit() and not char.isalpha():
            special_characters = True
            print("Password must consist only of letters and digits")
            break
    if digits_count < 2:
        fulfilled = False
        print("Password must have at least 2 digits")
    if special_characters:
        fulfilled = False
    if fulfilled:
        print("Password is valid")


password_from_console = input()

password_validator(password_from_console)