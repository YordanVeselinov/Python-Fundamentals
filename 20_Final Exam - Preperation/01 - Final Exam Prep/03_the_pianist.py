number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split("|")
    pieces[current_piece] = {"composer": current_composer, "key": current_key}

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    action = command[0]
    if action == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pieces.keys():
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')
    elif action == "Remove":
        piece = command[1]
        if piece not in pieces.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            pieces.pop(piece)
    elif action == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece not in pieces.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Changed the key of {piece} to {new_key}!")
            pieces[piece]["key"] = new_key
for current_piece, composer_key in pieces.items():
    print(f"{current_piece} -> Composer: {composer_key['composer']}, Key: {composer_key['key']}")
