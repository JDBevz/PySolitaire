#Solitaire in python : cards
import random
#Cards need a value, suit, (and colour?).
suits = ['C','H','S','D']
values = ['A', '1','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.faceUp = False

    def flip(self):
        self.faceUp = not self.faceUp

    def __str__(self):
        return '{0} {1} Face up? : {2}'.format(self.value, self.suit, self.faceUp)

#two kinds of pile, suit pile and play pile
class Pile:
    def __init__(self):
        self.cards = []

    def addCard(self, Card):
        self.cards.append(Card)

    def printPile(self):
        for x in self.cards :
            print(x)


class Deck:
    def __init__(self):
        self.cards = []

    #def setDeck

    def drawNext(self):
        None

    def removeCard(self):
        None

    def shuffleDeck(self):
        random.shuffle(self.cards)
