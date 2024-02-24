groceries = input().split("!")
while True:
    command = input().split()
    if command[0] == "Go" and command[1] == "Shopping!":
        break
    elif command[0] == "Urgent":
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif command[0] == "Correct":
        old_name = command[1]
        new_name = command[2]
        if old_name in groceries:
            index = groceries.index(old_name)
            groceries[index] = new_name
    elif command[0] == "Rearrange":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)


print(", ".join(groceries))