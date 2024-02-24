coffies = input().split()
number_of_commands = int(input())
for current_command in range(number_of_commands):
    command = input().split()
    action = command[0]
    if action == "Include":
        coffee_item = command[1]
        coffies.append(coffee_item)
    elif action == "Remove":
        number_of_coffies = int(command[2])
        counter = 0
        if command[1] == "first" and number_of_coffies < len(coffies):
            for current_item_index in range(len(coffies)):
                counter += 1
                coffies.pop(0)
                if counter == number_of_coffies:
                    break
        elif command[1] == "last" and number_of_coffies < len(coffies):
            for current_item_index in range(len(coffies)):
                counter += 1
                coffies.pop(-1)
                if counter == number_of_coffies:
                    break
    elif action == "Prefer":
        index_one = int(command[1])
        index_two = int(command[2])
        if 0 <= index_one < len(coffies) and 0 <= index_one < len(coffies):
            coffies[index_one], coffies[index_two] = coffies[index_two], coffies[index_one]
    elif action == "Reverse":
        coffies = [x for x in coffies[::-1]]
print("Coffees:")
print(" ".join(coffies))
