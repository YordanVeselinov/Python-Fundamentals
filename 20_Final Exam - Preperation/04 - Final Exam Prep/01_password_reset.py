sequence = input()

while True:
    command = input().split()
    if command[0] == "Done":
        break
    action = command[0]
    if action == "TakeOdd":
        index = 0
        new_sequence = ""
        for char in sequence:
            if index % 2 != 0:
                new_sequence += char
            index += 1
        sequence = new_sequence
        print(sequence)

    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        substring = sequence[index:index+length]
        sequence = sequence.replace(substring, "")
        print(sequence)

    elif action == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in sequence:
            sequence = sequence.replace(substring, substitute)
            print(sequence)
        else:
            print(f"Nothing to replace!")

print(f'Your password is: {sequence}')