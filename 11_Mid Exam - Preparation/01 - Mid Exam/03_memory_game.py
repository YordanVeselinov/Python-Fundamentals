sequence = input().split()
moves = 0
while True:
    moves += 1
    command = input()
    if command == 'end':
        break
    new_command = command.split()
    index_one = int(new_command[0])
    index_two = int(new_command[1])
    if (index_one < 0 or
            index_two >= len(sequence) or
            index_one >= len(sequence) or
            index_two < 0 or
            index_two == index_one):
        middle_index = len(sequence) // 2
        sequence.insert(middle_index, f"-{moves}a")
        sequence.insert(middle_index, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    if sequence[index_one] == sequence[index_two]:
        temp_element = sequence[index_two]
        sequence.pop(index_one)
        sequence.remove(temp_element)
        print(f"Congrats! You have found matching elements - {temp_element}!")
    else:
        print("Try again!")
    if not sequence:
        print(f"You have won in {moves} turns!")
        exit()

print(f"Sorry you lose :(")
print(" ".join(sequence))
