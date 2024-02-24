sequence = input()
last_character = ''
new_sequence = ""
for current_character in sequence:
    if current_character != last_character:
        new_sequence += current_character
        last_character = current_character
print(new_sequence)