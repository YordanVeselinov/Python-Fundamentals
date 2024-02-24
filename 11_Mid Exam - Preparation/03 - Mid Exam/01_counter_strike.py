initial_energy = int(input())
battle_wons = 0
is_game_ended = False
while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if distance <= initial_energy:
        battle_wons += 1
        initial_energy -= distance
    else:
        is_game_ended = True
        break
    if battle_wons % 3 == 0:
        initial_energy += battle_wons



if is_game_ended:
    print(f"Not enough energy! Game ends with {battle_wons} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battle_wons}. Energy left: {initial_energy}")
