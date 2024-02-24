first_word = input()
second_word = input()
last_printed = first_word

for char_index in range(len(first_word)):
    left_part = second_word[0:char_index+1]
    right_part = first_word[char_index+1:]
    new_word = left_part + right_part
    if new_word != last_printed:
        print(new_word)
        last_printed = new_word

