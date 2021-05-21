deck_list = input().split()
shuffles = int(input())

for _ in range(shuffles):
    current_deck = []
    half = int(len(deck_list)/2)
    first_half = deck_list[0:half]
    second_half = deck_list[half::]
    for card in range(len(first_half)):
        current_deck.append(first_half[card])
        current_deck.append(second_half[card])
    deck_list = current_deck

print(deck_list)
