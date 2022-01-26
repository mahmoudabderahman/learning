from operator import le
from pythonic_card_dick import Card, FrenchDeck

# create a beer_card
beer_card = Card('7', 'diamonds')
print(beer_card)

# calculate the number of the french deck cards
deck = FrenchDeck()
print(len(deck))

# easily get the first and last cards
print(deck[0])
print(deck[-1])

# randomly get a card with the random.choice from the Python data model
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

# look at the top three cards from a brand-new deck, and then pick just the Aces
print(deck[:3])
print(deck[12::13])

# iterate over the deck
for card in deck:
    print(card)


# iterate over the deck reversed
for card in reversed(deck):
    print(card)


# in works with our Frenchdeck class because it is iterable
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

