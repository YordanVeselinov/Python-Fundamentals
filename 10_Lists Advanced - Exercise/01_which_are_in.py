first_sequences = [word for word in input().split(", ")]
second_sequences = [word for word in input().split(", ")]
filtered_sequences = []
for first in first_sequences:
    for second in second_sequences:
        if first in second:
            filtered_sequences.append(first)
            break
print(filtered_sequences)
