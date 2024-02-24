word = input()
word_dict = {}

for current in word:
    if current not in word_dict and current != " ":
        word_dict[current] = 1
    elif current in word_dict and current != " ":
        word_dict[current] += 1

for key, value in word_dict.items():
    print(f"{key} -> {value}")