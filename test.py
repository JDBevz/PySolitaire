#Solitaire testing
from cards import *

#create 7 play piles, 4 set piles
#shuffle deck
#place cards into piles : index + 1 cards into pile, last card flipped up

pile = Pile()
pile.addCard(Card('A', 'C'))
pile.addCard(Card('K','S'))

pile.printPile()

x = Card('C', 'E')
print(x)
"""
playPiles = []
suitPiles = []
deck = Deck()
deck.resetDeck()
deck.shuffleDeck()

for i in range(7):
    playPiles.append(Pile())

for i in range(4):
    suitPiles.append(Pile())

for x in range(7):
    for y in range(x+1):
        playPiles[x].cards.append(deck.cards.pop())
    playPiles[x].cards[-1].flip()

for x in playPiles:
    print('\n')
    x.printPile()
"""
