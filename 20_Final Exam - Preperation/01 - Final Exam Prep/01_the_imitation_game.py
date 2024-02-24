encrypted_message = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    if command[0] == "Move":
        number_of_letter = int(command[1])
        encrypted_message = encrypted_message[number_of_letter:] + encrypted_message[:number_of_letter]
    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
print(f"The decrypted message is: {encrypted_message}")