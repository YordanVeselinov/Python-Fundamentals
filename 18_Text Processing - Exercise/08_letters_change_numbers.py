sum_of_all = 0
sequence = input().split()
for word in sequence:
    result = 0
    digit = ""
    front_letter = ""
    back_letter = ""
    for index in range(len(word)):
        if word[index].isdigit():
            digit += word[index]
            if front_letter == "":
                front_letter = word[index-1]
        if word[index].isdigit() and word[index+1].isalpha():
            back_letter = word[index+1]
    if front_letter.isupper():
        result = (float(digit) / (ord(front_letter) - 64))
    elif front_letter.islower():
        result = (float(digit) * (ord(front_letter) - 96))
    if back_letter.isupper():
        result -= (ord(back_letter) - 64)
    elif back_letter.islower():
        result += (ord(back_letter) - 96)
    sum_of_all += result
print(f"{sum_of_all:.2f}")

