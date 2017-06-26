# step_04_beat_the_black_jack.py
from collections import *
from random import *

# get a new deck
deck = Counter(tens=16, low=36)
deck = list(deck.elements())

# deal all cards
deal = sample(deck, 52)

# focus on the cards after 20 dealt out ones
remainder = deal[20:]
print(Counter(remainder))

# if more lows than tens, bid low;
# otherwise bit high
