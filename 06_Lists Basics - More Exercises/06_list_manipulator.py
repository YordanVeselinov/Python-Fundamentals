list_of_number = [int(i) for i in input().split()]
while True:
    command = input().split()
    if command[0] == 'end':
        break
    action = command[0]
    if action == "exchange":
        index = int(command[1])
        if len(list_of_number) > index >= 0:
            left_side = list_of_number[index+1:]
            right_side = list_of_number[:index+1]
            list_of_number = left_side + right_side
        else:
            print(f"Invalid index")

    elif action == "max":
        if command[1] == "even":
            maximum_number = [i for i in list_of_number if i % 2 == 0]
            if maximum_number:
                print(list_of_number.index(max(maximum_number)))
            else:
                print("No matches")
        elif command[1] == "odd":
            maximum_number = [i for i in list_of_number if i % 2 != 0]
            if maximum_number:
                print(list_of_number.index(max(maximum_number)))
            else:
                print("No matches")

    elif action == "min":
        if command[1] == "even":
            minimum_number = [num for num in list_of_number if num % 2 == 0]
            if minimum_number:
                print(list_of_number.index(min(minimum_number)))
            else:
                print("No matches")
        elif command[1] == "odd":
            minimum_number = [i for i in list_of_number if i % 2 != 0]
            if minimum_number:
                print(list_of_number.index(min(minimum_number)))
            else:
                print("No matches")
    elif action == "first":
        count = int(command[1])
        if count <= len(list_of_number):
            if command[2] == "even":
                even_number = []
                for current_index in range(count):
                    if list_of_number[current_index] % 2 == 0:
                        even_number.append(list_of_number[current_index])
                print(even_number)
            elif command[2] == "odd":
                odd_number = []
                for current_index in range(count):
                    if list_of_number[current_index] % 2 != 0:
                        odd_number.append(list_of_number[current_index])
                print(odd_number)
        else:
            print(f"Invalid count")
    elif action == "last":
        count = int(command[1])
        help_counter = 1
        if count <= len(list_of_number):
            if command[2] == "even":
                even_number = []
                for current_number in list_of_number[::-1]:
                    if current_number % 2 == 0:
                        even_number.append(current_number)
                    if help_counter == count:
                        break
                    help_counter += 1
                print(even_number)
            elif command[2] == "odd":
                odd_number = []
                for current_number in list_of_number[::-1]:
                    if current_number % 2 != 0:
                        odd_number.append(current_number)
                    if help_counter == count:
                        break
                    help_counter += 1
                print(odd_number)

        else:
            print(f"Invalid count")
print(list_of_number)


