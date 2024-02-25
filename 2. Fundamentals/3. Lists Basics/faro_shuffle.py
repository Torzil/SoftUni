starting_deck = input().split()
shuffles = int(input())
shuffled_deck = []
deck_half = len(starting_deck) // 2

for shuffle in range(shuffles):
    shuffled_deck = []
    left_half = starting_deck[:deck_half]
    right_half = starting_deck[deck_half:]
    for card in range(0, deck_half):
        shuffled_deck.append(left_half[card])
        shuffled_deck.append(right_half[card])
    starting_deck = shuffled_deck

print(shuffled_deck)
