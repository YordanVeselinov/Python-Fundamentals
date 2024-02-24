budget = int(input())
sum = 0

while True:
    input_word = input()
    if input_word == "End":
        print("You bought everything needed.")
        break
    input_word = int(input_word)
    sum += input_word
    if sum > budget:
        print("You went in overdraft!")
        break