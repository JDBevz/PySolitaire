#Solitaire in python : cards
import random
#Cards need a value, suit, (and colour?).
suits = ['C','H','S','D']
values = ['A', '1','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __new__(cls, value, suit):
        if suit in suits and value in values:
            return object.__new__(cls)
        else:
            return None

    def __init__(self, value, suit):
            self.suit = suit
            self.value = value
            self.faceUp = False
            if suit == 'C' or 'S':
                self.colour = 'B'
            elif suit == 'H' or 'D':
                self.colour = 'R'

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

class PlayPile(Pile):
    def addPile(self, toAdd: Pile):
        if toAdd.cards[0].colour != self.cards[-1].colour:
            self.cards.append(toAdd)
        else:
            fail

class SuitPile(Pile):
    def __new__(cls, suit):
        if suit in suits:
            return object.__new__(cls)
        else:
            return None

    def __init__(self, suit):
        Pile.__init__(self)
        self.suit = suit

    def addCard(self, Card):
        if Card.suit != self.suit:
            return False
        else:
            self.cards.append(Card)

    def checkPile(self):
        for x in self.cards:
            if cards[x].suit != self.suit:
                return False
        return True

class Deck:
    def __init__(self):
        self.cards = []
        self.drawIndex = 0

    def resetDeck(self):
        for x in suits:
            for y in values:
                self.cards.append(Card(x,y))

    def drawNext(self):
        if drawIndex > len(self.cards):
            drawIndex = 0
        else:
            drawIndex = drawIndex+1
        pass

    def removeCard(self):
        pass

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def printDeck(self):
        for x in self.cards:
            print(x)
