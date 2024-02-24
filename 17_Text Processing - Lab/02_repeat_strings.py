words = input().split()
final_words = ""
counter = 0
for current_word in words:
    counter = len(current_word)
    final_words += current_word * counter
print(final_words)