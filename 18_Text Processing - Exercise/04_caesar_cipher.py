sequence = input()
new_sequence = ""
for character in sequence:
    new_sequence += chr(ord(character) + 3)
print(new_sequence)