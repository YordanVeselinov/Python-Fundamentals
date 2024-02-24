sequence = [int(i) for i in input().split()]
shots_targets = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if 0 <= index < len(sequence) and sequence[index] != -1:
        shot_value = sequence[index]
        sequence[index] = -1
        shots_targets += 1
        for current_index in range(len(sequence)):
            if sequence[current_index] > shot_value and sequence[current_index] != -1:
                sequence[current_index] -= shot_value
            elif sequence[current_index] <= shot_value and sequence[current_index] != -1:
                sequence[current_index] += shot_value

print(f"Shot targets: {shots_targets} -> {' '.join(map(str, sequence))}")
