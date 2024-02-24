import re
sequence = input()
pattern = r"([:*]{2})([A-Z][a-z]{2,})\1"
cool_threshold = re.findall("\d", sequence)
threshold = 1
matches = re.findall(pattern, sequence)

for number in cool_threshold:
    threshold *= int(number)
print(f'Cool threshold: {threshold}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')
for emojis in matches:
    emoji_sum = 0
    for char in emojis[1]:
        emoji_sum += ord(char)
    if emoji_sum >= threshold:
        print(f"{emojis[0]}{emojis[1]}{emojis[0]}")