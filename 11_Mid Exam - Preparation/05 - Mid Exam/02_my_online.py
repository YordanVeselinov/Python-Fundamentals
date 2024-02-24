rooms = input().split("|")
initial_health = 100
bitcoin = 0
is_dead = False
for current_room in rooms:
    room = rooms.index(current_room)
    current_room = current_room.split()
    command, number = current_room[0], int(current_room[1])
    if command == "potion":
        temp_health = initial_health
        initial_health += number
        if initial_health > 100:
            initial_health = 100
            healed = initial_health - temp_health
        else:
            healed = number
        print(f"You healed for {healed} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        if initial_health > number:
            initial_health -= number
            print(f"You slayed {command}.")
        else:
            is_dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room+1}")
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {initial_health}")



