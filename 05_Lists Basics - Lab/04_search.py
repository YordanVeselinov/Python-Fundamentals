number_of_integrations = int(input())
special_word = input()
all_words = []
filtered_words = []
for _ in range(number_of_integrations):
    command = input()
    all_words.append(command)
    if special_word in command:
        filtered_words.append(command)

print(all_words)
print(filtered_words)