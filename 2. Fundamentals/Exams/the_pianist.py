number_of_pieces = int(input())

collection = {}

for new_piece in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split("|")
    collection[current_piece] = {"Composer": current_composer, "Key": current_key}

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split("|")
    action = command[0]

    if action == "Add":
        piece = command[1]
        composer = command[2]
        music_key = command[3]
        if piece not in collection:
            collection[piece] = {"Composer": composer, "Key": music_key}
            print(f"{piece} by {composer} in {music_key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece in collection:
            print(f"Successfully removed {piece}!")
            del collection[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command[1]
        new_music_key = command[2]
        if piece in collection:
            collection[piece]["Key"] = new_music_key
            print(f"Changed the key of {piece} to {new_music_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key in collection.keys():
    piece_composer = collection[key]["Composer"]
    piece_key = collection[key]["Key"]
    print(f"{key} -> Composer: {piece_composer}, Key: {piece_key}")
