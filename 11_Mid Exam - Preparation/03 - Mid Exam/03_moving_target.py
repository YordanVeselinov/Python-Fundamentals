def valid_index(list_of_items, current_index):
    return (
            0 <= current_index < len(list_of_items)
    )


sequence = [int(x) for x in input().split()]
while True:
    command = input().split()
    if command[0] == "End":
        break
    index = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if valid_index(sequence, index):
            sequence[index] -= value
            if sequence[index] <= 0:
                sequence.pop(index)

    elif command[0] == "Add":
        if valid_index(sequence, index):
            sequence.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if valid_index(sequence, index) and index + value < len(sequence) and index - value >= 0:
            start = index - value
            finish = index + value + 1
            for current in sequence[start:finish]:
                sequence.remove(current)

        else:
            print("Strike missed!")
print("|".join(map(str,sequence)))
