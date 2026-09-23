# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
'''__len__ and __getitem__ make an object act as a sequence'''

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

deck = Deck(['ace', 'king', 'queen'])
print(len(deck))
print(deck[0], deck[-1])
for card in deck:
    print(card)
print('king' in deck)
