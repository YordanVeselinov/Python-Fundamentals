banned_word = input().split(", ")
sequence = input()
for current_word in banned_word:
    while current_word in sequence:
        sequence = sequence.replace(current_word,"*" * len(current_word))
print(sequence)