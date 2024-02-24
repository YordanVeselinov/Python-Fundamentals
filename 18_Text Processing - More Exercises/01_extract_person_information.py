number_of_sentences = int(input())
name = ""
age = ""
name_found = False
age_found = False
for current in range(number_of_sentences):
    sentence = input()
    for index in range(len(sentence)):
        if sentence[index] == "@":
            for index_name in range(index+1, len(sentence)):
                if sentence[index_name] == "|":
                    name_found = True
                    break
                name += sentence[index_name]
        elif sentence[index] == "#":
            for index_name in range(index+1, len(sentence)):
                if sentence[index_name] == "*":
                    age_found = True
                    break
                age += sentence[index_name]
        if name_found and age_found:
            print(f"{name} is {age} years old.")
            name_found = False
            age_found = False
            name = ""
            age = ""
            break

