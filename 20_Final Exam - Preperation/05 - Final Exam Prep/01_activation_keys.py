string = input()
while True:
    command = input().split(">>>")
    if command[0] == 'Generate':
        break
    action = command[0]
    if action == 'Contains':
        substring = command[1]
        if substring in string:
            print(f"{string} contains {substring}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        upper_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        if upper_lower == "Upper":
            string = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
        elif upper_lower == "Lower":
            string = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
        print(string)
    elif action == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        string = string[:start_index] + string[end_index:]
        print(string)
print(f"Your activation key is: {string}")