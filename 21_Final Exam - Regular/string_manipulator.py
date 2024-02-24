string = input()
while True:
    command = input().split()
    if command[0] == "End":
        break

    action = command[0]
    if action == "Translate":
        char, replacement = command[1], command[2]
        string = string.replace(char, replacement)
        print(string)
    elif action == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif action == "Start":
        substring = command[1]
        if string.startswith(substring):
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        string = string.lower()
        print(string)
    elif action == "FindIndex":
        char = command[1]
        for current_char in string[::-1]:
            if char == current_char:
                print(string.index(current_char))
                break
    elif action == "Remove":
        start_index, count = int(command[1]), int(command[2])
        remove_string = string[start_index:count+start_index]
        string = string.replace(remove_string, "")
        print(string)