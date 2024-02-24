words = [word for word in input().split()]
new_word = []
for current_word in words:
    digit = ""
    string = []
    for current_digit in current_word:
        if current_digit.isdigit():
            digit += current_digit
        else:
            string += current_digit
    string[0], string[-1] = string[-1], string[0]
    digit = chr(int(digit))
    new_word.append(digit+"".join(string))

print(" ".join(new_word))
