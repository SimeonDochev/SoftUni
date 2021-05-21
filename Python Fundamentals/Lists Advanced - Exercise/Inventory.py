def collect_item(items_list, item):
    items_list.append(item)


def drop_item(items_list, item):
    items_list.remove(item)


def combine_items(items_list, old_item, new_item):
    old_item_index = items_list.index(old_item)
    items_list.insert(old_item_index+1, new_item)


def renew_item(items_list, item):
    items_list.remove(item)
    items_list.append(item)


inventory = input().split(", ")

command = input()
while not command == "Craft!":
    command_data = command.split(" - ")
    action, item_from_command = command_data[0], command_data[1]
    if action == "Collect":
        if item_from_command not in inventory:
            collect_item(inventory, item_from_command)
    elif action == "Drop":
        if item_from_command in inventory:
            drop_item(inventory, item_from_command)
    elif action == "Combine Items":
        item1, item2 = command_data[1].split(":")
        if item1 in inventory:
            combine_items(inventory, item1, item2)
    elif action == "Renew":
        if item_from_command in inventory:
            renew_item(inventory, item_from_command)
    command = input()

print(*inventory, sep=", ")
