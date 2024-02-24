sequence_of_number = [int(num) for num in input().split()]

while True:
    index = 0
    new_sequence = ""
    type = ""
    type_found = False
    coordinates = ""
    coordinates_found = False
    line = input()
    if line == "find":
        break
    for char in line:
        if index > len(sequence_of_number) - 1:
            index = 0
        new_sequence += chr(ord(char) - sequence_of_number[index])
        index += 1
    for current_index in range(len(new_sequence)):
        if new_sequence[current_index] == "&" and not type_found:
            for new_index in range(current_index + 1, len(new_sequence)):
                if new_sequence[new_index] == "&":
                    type_found = True
                    break
                type += new_sequence[new_index]
        elif new_sequence[current_index] == "<" and not coordinates_found:
            for new_index in range(current_index + 1, len(new_sequence)):
                if new_sequence[new_index] == ">":
                    coordinates_found = True
                    break
                coordinates += new_sequence[new_index]
        if type_found and coordinates_found:
            break
    print(f"Found {type} at {coordinates}")
