string = [word for word in input().split()]

while True:
    command = input().split()
    new_string = []
    if command[0] == '3:1':
        break
    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(string) - 1:
            end_index = len(string) - 1
        merged_string = "".join(string[start_index:end_index+1])
        string[start_index:end_index+1] = [merged_string]

    elif command[0] == 'divide':
        index = int(command[1])
        partition = int(command[2])
        element = string[index]
        divided_partition = []
        partition_length = len(element) // partition
        for current_index in range(partition):
            if current_index != partition - 1:
                divided_partition.append(element[current_index * partition_length: (current_index+1) * partition_length])
            else:
                divided_partition.append(element[current_index * partition_length:])
        string[index:index+1] = divided_partition

print(" ".join(string))