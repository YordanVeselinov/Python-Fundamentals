first_char = input()
second_char = input()
sequence = input()
result = 0

for char in sequence:
    if ord(first_char) < ord(char) < ord(second_char):
        result += ord(char)

print(result)