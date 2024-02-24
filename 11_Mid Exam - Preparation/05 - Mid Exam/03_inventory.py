items = input().split(", ")
while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break
    if command[0] == "Collect":
        item = command[1]
        if item not in items:
            items.append(item)
    elif command[0] == "Drop":
        item = command[1]
        if item in items:
            items.remove(item)
    elif command[0] == "Combine Items":
        two_items = command[1].split(":")
        item_old = two_items[0]
        item_new = two_items[1]
        if item_old in items:
            index = items.index(item_old)
            items.insert(index+1, item_new)
    elif command[0] == "Renew":
        item = command[1]
        if item in items:
            items.remove(item)
            items.append(item)

print(", ".join(items))