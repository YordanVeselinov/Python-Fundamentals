sequence = input()
digit = ""
letter = ""
other_symbol = ""
for current_symbol in sequence:
    if current_symbol.isdigit():
        digit += current_symbol
    elif current_symbol.isalpha():
        letter += current_symbol
    else:
        other_symbol += current_symbol
print(digit)
print(letter)
print(other_symbol)