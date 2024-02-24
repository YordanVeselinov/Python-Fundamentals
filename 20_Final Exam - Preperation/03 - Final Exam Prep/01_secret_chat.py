concealed_message = input()

while True:
    command = input().split(":|:")
    if command[0] == 'Reveal':
        break
    action = command[0]
    if action == 'InsertSpace':
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "")
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print(f"error")
    elif action == 'ChangeAll':
        substring, replacement = command[1], command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
print(f"You have a new text message: {concealed_message}")