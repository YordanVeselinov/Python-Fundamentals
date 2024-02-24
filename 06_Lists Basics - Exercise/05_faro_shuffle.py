deck_of_cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    deck_after_shuffle = []
    for index in range(len(left_part)):
        deck_after_shuffle.append(left_part[index])
        deck_after_shuffle.append(right_part[index])
    deck_of_cards = deck_after_shuffle
print(deck_after_shuffle)