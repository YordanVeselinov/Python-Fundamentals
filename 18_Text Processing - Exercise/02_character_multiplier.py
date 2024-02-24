one_word, two_word = input().split()
sum_of_words = 0

if len(one_word) == len(two_word):
    for index in range(len(one_word)):
        sum_of_words += ord(one_word[index]) * ord(two_word[index])
elif len(one_word) > len(two_word):
    for index in range(len(two_word)):
        sum_of_words += ord(one_word[index]) * ord(two_word[index])
    for index in range(len(two_word), len(one_word)):
        sum_of_words += ord(one_word[index])
else:
    for index in range(len(one_word)):
        sum_of_words += ord(one_word[index]) * ord(two_word[index])
    for index in range(len(one_word), len(two_word)):
        sum_of_words += ord(two_word[index])


print(sum_of_words)

