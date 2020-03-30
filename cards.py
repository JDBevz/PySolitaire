#Solitaire in python : cards
import random
#Cards need a value, suit, (and colour?).
suits = ['C','H','S','D']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def valueSort(x):
    return values.index(x.value)
def suitSort(x):
    return suits.index(x.suit)
#sort in CHaSeD order by value. Probably a better way to do it but this works consistently


class Card:
    def __new__(cls, value, suit, faceUp = False):
        if suit in suits and value in values:
            return object.__new__(cls)
        else:
            return None

    def __init__(self, value, suit, faceUp = False):
            self.suit = suit
            self.value = value
            self.faceUp = faceUp
            if suit in ['C', 'S']:
                self.colour = 'B'
            elif suit in ['H', 'D']:
                self.colour = 'R'

    def flip(self):
        self.faceUp = not self.faceUp

    def __str__(self):
        if self.faceUp:
            return '[{0} {1} {2}]'.format(self.value, self.suit, self.colour)
        else:
            return '[#]'

#two kinds of pile, suit pile and play pile
class Pile:
    def __init__(self):
        self.cards = []

    def addCard(self, Card):
        self.cards.append(Card)

    def printPile(self):
        for x in self.cards :
            print(x)

    def __str__(self):
        for x in self.cards:
            return'{}'.format(x)

class PlayPile(Pile):

    def addCards(self, toAdd):
        print("Self : %s Add: %s"%(self.cards[-1].colour, toAdd[0].colour))
        print(toAdd[-1])
        print(self.cards[-1])
        if toAdd[-1].colour != self.cards[-1].colour:
            self.cards.extend(toAdd)
            return True
        else:
            print('Cannot add pile')
            return False

    def getBottomPlayCardIndex(self):
        if self.cards:
            i = 0
            while i > -len(self.cards):
                if self.cards[i-1].faceUp == False:
                    return i
                else:
                    i-=1


            i = 0
            while i < len(self.cards):
                if self.cards[i].faceUp == False :
                    i += 1
                else:
                    return i
        elif not self.cards:
            None

class SuitPile(Pile):
    def __new__(cls, suit):
        if suit in suits:
            return object.__new__(cls)
        else:
            return None

    def __init__(self, suit):
        Pile.__init__(self)
        self.suit = suit

    def addCard(self, card):
        if self.suit == card.suit:
            if not self.cards and card.value == 'A':
                self.cards.append(card)
                return True
            elif valueSort(self.cards[0])+1 == valueSort(card):
                self.cards.append(card)
                return True
        return False


    def getTopCard(self):
        if self.cards :
            return self.cards[-1]
        else :
            return '___'

    def checkPile(self):
        for x in self.cards:
            if cards[x].suit != self.suit:
                return False
        return True

class Deck:
    def __init__(self):
        self.cards = []
        self.drawIndex = -1

    def resetDeck(self):
        for x in suits:
            for y in values:
                self.cards.append(Card(y,x))

    def drawNext(self):
            if self.drawIndex == len(self.cards)-1:
                self.drawIndex = 0
                for x in self.cards:
                    x.faceUp = False
            else:
                self.drawIndex = self.drawIndex+1
            self.cards[self.drawIndex].flip()


    def getDrawCard(self):
        if self.cards:
            return self.cards[self.drawIndex]
        else :
            return False

    def removeCard(self):
        if(self.cards):
            pop(self.drawIndex)
            self.drawIndex-1
            if(self.drawIndex < 0):
                drawIndex = 0
        else :
            return False
        pass

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def printDeck(self):
        for x in self.cards:
            print(x, end = ' ')
        print('\n')
