participants = {}
languages = {}

banned_users = []

command = input()
while not command == "exam finished":
    command_data = command.split("-")
    user = command_data[0]
    if "banned" in command_data:
        banned_users.append(user)
        participants.pop(user)
    else:
        language = command_data[1]
        points = int(command_data[2])
        if user not in participants and user not in banned_users:
            participants[user] = points
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
        elif user in participants and user not in banned_users:
            languages[language] += 1
            if points > participants[user]:
                participants[user] = points
    command = input()

print("Results:")
for participant, points in sorted(participants.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{participant} | {points}")
print("Submissions:")
for language, submissions in sorted(languages.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{language} - {submissions}")
