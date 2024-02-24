list_of_gifts = input().split()
command = input().split()
while command[0] != "No" and command[1] != "Money":
    if "OutOfStock" in command:
        for index, item in enumerate(list_of_gifts):
            if item == command[1]:
                list_of_gifts[index] = "None"
    elif "Required" in command:
        for i in range(len(list_of_gifts)):
            if i == int(command[2]):
                list_of_gifts[i] = command[1]

    elif "JustInCase" in command:
        list_of_gifts[-1] = command[1]

    command = input().split()

while "None" in list_of_gifts:
        list_of_gifts.remove("None")
print(" ".join(list_of_gifts))

