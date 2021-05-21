import re

pattern = r"([a-zA-Z0-9\W+]+)>(?P<password>[\d]{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1"

n = int(input())
for _ in range(n):
    text = input()
    matches = re.match(pattern, text)
    if not matches:
        print("Try another password!")
    else:
        valid_password = re.finditer(pattern, text)
        for obj in valid_password:
            password = obj.group('password')
            final_password = password.replace('|', '')
            print(f"Password: {final_password}")
