import random

random.seed(42)
deck = ['ace', 'king', 'queen', 'jack']
random.shuffle(deck)
print(deck)

print(random.sample(range(1, 50), 6))
print(random.choices(['heads', 'tails'], k=5))
