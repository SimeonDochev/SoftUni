import os


def create_file(filename):
    with open(filename, 'w'):
        pass


def add_to_file(filename, content):
    try:
        with open(filename, "a") as f:
            f.write(f"{content}\n")
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write(f"{content}\n")


def replace_text(filename, old_text, new_text):
    try:
        with open(filename, "r+") as f:
            text = f.read()
            text = text.replace(old_text, new_text)
        with open(filename, "w") as f:
            f.write(text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("An error occurred")


command = input()
while not command == "End":
    cmd_data = command.split('-')
    action = cmd_data[0]
    file_name = cmd_data[1]
    if action == "Create":
        create_file(file_name)
    elif action == "Add":
        content = cmd_data[2]
        add_to_file(file_name, content)
    elif action == "Replace":
        old_text = cmd_data[2]
        new_text = cmd_data[3]
        replace_text(file_name, old_text, new_text)
    elif action == "Delete":
        delete_file(file_name)
    command = input()
