users_data = {}

all_users = []

command = input()
while not command == "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        if side not in users_data.keys():
            users_data[side] = []
        if user not in users_data[side] and user not in all_users:
            users_data[side].append(user)
            all_users.append(user)
    elif "->" in command:
        user, side = command.split(" -> ")
        if side not in users_data.keys():
            users_data[side] = []
        if user not in users_data[side] and user not in all_users:
            users_data[side].append(user)
            all_users.append(user)
            print(f"{user} joins the {side} side!")
        elif user not in users_data[side] and user in all_users:
            users_data[side].append(user)
            all_users.append(user)
            print(f"{user} joins the {side} side!")
            for sides in users_data:
                if not sides == side and user in users_data[sides]:
                    users_data[sides].remove(user)
    command = input()

for sides, users in sorted(users_data.items(), key=lambda k: (-len(k[1]), k[0])):
    if len(users_data[sides]) > 0:
        print(f"Side: {sides}, Members: {len(users_data[sides])}")
        for user in sorted(users_data[sides]):
            print(f"! {user}")
