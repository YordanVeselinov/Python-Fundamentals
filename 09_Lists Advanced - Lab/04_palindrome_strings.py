secquens_of_word = input().split()
palindrome_word = input()

new_list = [item for item in secquens_of_word if item == item[::-1]]
coulter = 0
for item in new_list:
    if item == palindrome_word:
        coulter += 1
print(new_list)
print(f"Found palindrome {coulter} times")