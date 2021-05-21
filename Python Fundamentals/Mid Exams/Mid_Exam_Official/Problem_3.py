def chat(array, item):
    array.append(item)


def delete(array, item):
    array.remove(item)


def edit(array, old_item, new_item):
    i = array.index(old_item)
    array.remove(old_item)
    array.insert(i, new_item)


def pin(array, item):
    array.remove(item)
    array.append(item)


def spam(array, items):
    for item in items:
        array.append(item)


chat_history = []
command = input()
while not command == "end":
    command_data = command.split()
    action = command_data[0]
    if action == "Chat":
        message = command_data[1]
        chat(chat_history, message)
    elif action == "Delete":
        message = command_data[1]
        delete(chat_history, message)
    elif action == "Edit":
        old_message = command_data[1]
        new_message = command_data[2]
        edit(chat_history, old_message, new_message)
    elif action == "Pin":
        message = command_data[1]
        pin(chat_history, message)
    elif action == "Spam":
        messages = command_data[1::]
        spam(chat_history, messages)
    command = input()

print("\n".join(chat_history))
