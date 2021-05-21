def register(username, license_plate_number):
    database[username] = license_plate_number


def unregister(username):
    database.pop(username)


database = {}

n = int(input())
for _ in range(n):
    command_data = input().split()
    command = command_data[0]
    name = command_data[1]
    if command == "register":
        plate = command_data[2]
        if name in database:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            register(name, plate)
            print(f"{name} registered {plate} successfully")
    elif command == "unregister":
        if name not in database:
            print(f"ERROR: user {name} not found")
        else:
            unregister(name)
            print(f"{name} unregistered successfully")

for k, v in database.items():
    print(f"{k} => {v}")
