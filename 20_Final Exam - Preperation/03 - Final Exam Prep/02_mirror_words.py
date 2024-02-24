import re
sequence = input()
mirror_words = []
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(pattern, sequence)

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(match[1])
    elif match[1][::-1] == match[2]:
        mirror_words.append(match[2])
if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if mirror_words:
    index = 0
    print(f"The mirror words are:")
    for word in mirror_words:
        index += 1
        if index == len(mirror_words):
            print(f"{word} <=> {word[::-1]}")

        else:
            print(f"{word} <=> {word[::-1]},", end=" ")


else:
    print("No mirror words!")
