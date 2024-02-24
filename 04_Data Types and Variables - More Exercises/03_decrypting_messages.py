additional_number = int(input())
number_of_lines = int(input())
word = ""
for current_line in range(number_of_lines):
    current_digit = input()
    current_digit = ord(current_digit)
    word += chr(current_digit + additional_number)
print(word)
