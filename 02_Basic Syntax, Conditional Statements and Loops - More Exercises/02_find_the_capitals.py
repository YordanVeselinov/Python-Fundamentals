word = input()
list =[]

for index in range(len(word)):
    if word[index].isupper():
        list.append(index)
print(list)