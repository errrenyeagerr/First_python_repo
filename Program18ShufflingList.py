# Shuffles the order of the List.

import random
cards = ["Jack", "Queen", "King", "Ace", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
for card in cards:
    print (card)