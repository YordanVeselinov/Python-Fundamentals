list_of_orders = input().split("|")
coins = 100
energy = 100
is_closed = False

for current in list_of_orders:
    current_event = current.split("-")
    event = current_event[0]
    value = int(current_event[1])
    if event == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            print("You had to rest!")
            energy += 50


    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {event}.")

