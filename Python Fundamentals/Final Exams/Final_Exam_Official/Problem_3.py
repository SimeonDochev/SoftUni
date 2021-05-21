def new_follower(followers, username):
    if username not in followers:
        followers[username] = {'likes': 0, 'comments': 0}


def like(followers, username, count):
    if username not in followers:
        followers[username] = {'likes': count, 'comments': 0}
    else:
        followers[username]['likes'] += count


def comment(followers, username):
    if username not in followers:
        followers[username] = {'likes': 0, 'comments': 1}
    else:
        followers[username]['comments'] += 1


def blocked(followers, username):
    if username not in followers:
        print(f"{username} doesn't exist.")
    else:
        followers.pop(username)


followers = {}

command = input()
while not command == "Log out":
    command_data = command.split(': ')
    action = command_data[0]
    username = command_data[1]
    if action == "New follower":
        new_follower(followers, username)
    elif action == "Like":
        count = int(command_data[2])
        like(followers, username, count)
    elif action == "Comment":
        comment(followers, username)
    elif action == "Blocked":
        blocked(followers, username)
    command = input()

print(f"{len(followers)} followers")

for follower in followers:
    followers[follower]['total'] = followers[follower]['likes'] + followers[follower]['comments']

for follower, info in sorted(followers.items(), key=lambda kvp: (-kvp[1]['total'], kvp[0])):
    print(f"{follower}: {info['total']}")
