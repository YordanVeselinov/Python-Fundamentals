delete_word = input()
sequence = input()
while delete_word in sequence:
    sequence = sequence.replace(delete_word, "")
print(sequence)