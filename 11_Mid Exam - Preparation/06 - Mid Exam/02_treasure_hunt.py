loot = input().split("|")

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    if command[0] == "Loot":
        for current_item in command:
            if current_item not in loot and current_item != "Loot":
                loot.insert(0, current_item)
    elif command[0] == "Drop":
        index = int(command[1])
        if index < len(loot):
            removed = loot.pop(index)
            loot.append(removed)
    elif command[0] == "Steal":
        number = int(command[1])
        count_stolen = min(number, len(loot))
        counter = 0
        stolen = []
        for current in range(count_stolen, 0, -1):
            stolen.append(loot[-current])
            loot.remove(loot[-current])
        print(", ".join(stolen))

if len(loot) > 0:
    treasure_gain = 0
    for current_item in loot:
        treasure_gain += len(current_item)
    average_gain = treasure_gain / len(loot)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
else:
    print("Failed treasure hunt.")
