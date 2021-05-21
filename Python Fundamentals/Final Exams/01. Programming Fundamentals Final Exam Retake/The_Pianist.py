n = int(input())
collection = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    collection[piece] = [composer, key]

command = input()
while not command == "Stop":
    command_data = command.split("|")
    piece = command_data[1]
    if command_data[0] == "Add":
        composer = command_data[2]
        key = command_data[3]
        if piece not in collection:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command_data[0] == "Remove":
        if piece in collection:
            collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_data[0] == "ChangeKey":
        new_key = command_data[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for key, value in sorted(collection.items(), key=lambda kvp: (kvp[0], kvp[1][0])):
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
