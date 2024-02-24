conditions = ["a", "o", "u", "e", "i",]

word = input()
filtered_word = [char for char in word if char.lower() not in conditions ]
print("".join(filtered_word))