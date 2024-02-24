number_of_lists = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        number_of_lists[index_one], number_of_lists[index_two] = number_of_lists[index_two], number_of_lists[index_one]
    elif command[0] == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])
        number_of_lists[index_one] = number_of_lists[index_one] * number_of_lists[index_two]
    elif command[0] == "decrease":
        for index in range(len(number_of_lists)):
            number_of_lists[index] -= 1

print(", ".join(map(str,number_of_lists)))

