sequence = input()
for index in range(len(sequence)):
    if sequence[index] == ":":
        print(sequence[index]+ sequence[index+1])