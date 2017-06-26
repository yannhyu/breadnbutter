# step_03_deck_of_cards.py
from collections import *
from random import *

deck = Counter(tens=16, low=36)
print('new deck:')
print(deck)
print()

print('full deck:')
deck = list(deck.elements())
print(deck)
print()

print('deal of 20 cards')
deal = sample(deck, 20)
print(deal)
print(Counter(deal))