#Solitaire testing
from cards import *
from cmdtest import *
import os
import argparse
import cmd

#os.system('cls')

def printPiles(piles):
    i=1
    for x in piles:
        print(i,': ', end = '')
        if x.cards:
            for y in x.cards:
                print(y, end = '')
        else :
            print('___')
        i +=1
        print('\n')

def printDeck(deck):
    print('Deck : {}'.format(deck.getDrawCard()))

def printSuitPiles(suitPiles):
    for x in suitPiles:
        print('{0}: {1}'.format(x.suit, x.getTopCard()), end = ' ')
    pass

def printPlay(playPiles, suitPiles, deck):
    #os.system('cls')
    printDeck(deck)
    printPiles(playPiles)
    printSuitPiles(suitPiles)


def printList(a):
    for x in a:
        print(x)

#get the top revealed card
def getBottomPlayCard(pile):
    if pile.cards:
        i = 0
        while i < len(pile.cards):
            if pile.cards[i].faceUp == False :
                i += 1
            else:
                return i
    elif not pile.cards:
        None

# moves entire playable pile from a -> b
def movePP(a, b):
    if a.cards:
        aIndex = a.getBottomPlayCardIndex()
        if b.cards or (not b.cards and a.cards[aIndex].value == 'K'):
            if b.addCards(a.cards[aIndex:]):
                del a.cards[aIndex:]
                if a.cards:
                    if not a.cards[-1].faceUp:
                        a.cards[-1].flip()

def movePP(a, b, index):
    if a.cards:

            if b.addCards(a.cards[-index:]):
                del a.cards[-index:]
                if a.cards:
                    if not a.cards[-1].faceUp:
                        a.cards[-1].flip()

def moveDP(d, p):
    if deck.cards:
        pass

#move index number of cards from a to b. Count up from the bottom
#ie : 1 will move only the bottom card
#current : assume no problems with chosen index

#handle any move in one function
def move(a, b, index = False):
    if a.cards:
        #move from deck
        if isinstance(a, Deck):
            if(b.addCard(a.getDrawCard())):
                a.removeCard()
            else:
                return False

        #move from a play pile
        elif isinstance(a, PlayPile):
            #from play to play
            if isinstance(b, PlayPile):
                if b.cards or (not b.cards and a.cards[-index].value == 'K'):
                    if not index:
                        index = a.getBottomPlayCardIndex()

                    if b.addCards(a.cards[index:]):
                        print(index)
                        del a.cards[index:]
                        if a.cards:
                            if not a.cards[-1].faceUp:
                                a.cards[-1].flip()

            #from play to suit
            elif isinstance(b, SuitPile):
                index = -1

                if b.addCard(a.cards[-1]):
                    del(a.cards[-1])
                    if not a.cards[-1].faceUp:
                        a.cards[-1].flip()

#move a card from a play pile to a suit pile
def moveSP(pp , sp):
    if sp.addCard(pp.cards[-1]):
        del(pp.cards[-1])
        if not pp.cards[-1].faceUp:
            pp.cards[-1].flip()


def printMenu():
    print('move from to\ndraw')
    pass

#action types :
#move deck (to) pile#
#move pile# (to) pile#
#move pile# (to) suit
#draw
"""
def processAction(self, action):
    if action[0] == 'd': #draw
        deck.drawNext()

    elif action[0] == 'm': #move
        if #'d':
            drawCard = deck.getDrawCard()
            movePP(drawCard, pile)
        if #int:
            if #'CHSD'
            elif #int
        pass
    pass
"""
#create 7 play piles, 4 set piles
#shuffle deck
#place cards into piles : index + 1 cards into pile, last card flipped up

playPiles = []
suitPiles = []
deck = Deck()
deck.resetDeck()
deck.shuffleDeck()

for i in range(7):
    playPiles.append(PlayPile())

for i in suits:
    suitPiles.append(SuitPile(i))

for x in range(7):
    for y in range(x+1):
        playPiles[x].cards.append(deck.cards.pop())
    playPiles[x].cards[-1].flip()

    deck.drawNext()


if __name__ == '__main__':
    SolitaireCmdShell().cmdloop()
