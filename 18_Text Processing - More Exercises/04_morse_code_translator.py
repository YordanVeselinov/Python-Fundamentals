words_in_morse_code = input().split("|")
english_sentence = []
word = ""

for current_word_morse in words_in_morse_code:
    word = ""
    letters = current_word_morse.split()
    for letter in letters:
        if letter == ".-":
            word += "A"
        elif letter == "-...":
            word += "B"
        elif letter == "-.-.":
            word += "C"
        elif letter == "-..":
            word += "D"
        elif letter == ".":
            word += "E"
        elif letter == "..-.":
            word += "F"
        elif letter == "--.":
            word += "G"
        elif letter == "....":
            word += "H"
        elif letter == "..":
            word += "I"
        elif letter == ".---":
            word += "J"
        elif letter == "-.-":
            word += "K"
        elif letter == ".-..":
            word += "L"
        elif letter == "--":
            word += "M"
        elif letter == "-.":
            word += "N"
        elif letter == "---":
            word += "O"
        elif letter == ".--.":
            word += "P"
        elif letter == "--.-":
            word += "Q"
        elif letter == ".-.":
            word += "R"
        elif letter == "...":
            word += "S"
        elif letter == "-":
            word += "T"
        elif letter == "..-":
            word += "U"
        elif letter == "...-":
            word += "V"
        elif letter == ".--":
            word += "W"
        elif letter == "-..-":
            word += "X"
        elif letter == "-.--":
            word += "Y"
        elif letter == "--..":
            word += "X"
    english_sentence.append(word.upper())
print(" ".join(english_sentence))