#solitaire game logic
from cards import *

#initialize needed objects


#create 7 play piles, 4 set piles
#shuffle deck
#place cards into piles : index + 1 cards into pile, last card flipped up
playPiles = []

for i in range(7):
    playPiles.append(Pile())

#Actions needed for play :
    # move pile from a -> b
        # move(a, b)
        # check that chosen pile can be moved
    # draw card (Deck.drawNext)
        # show next card in Deck
        # if no more cards, loop back to the start of the deck
    # move draw card to pile
    # move bottom card to suit pile
    # split pile (and move)
        # move(a, b, split)
        # split counted from the 'bottom' of the pile, ie: number of cards to move






#Auto play order:
#move kings to empty :
    #Move any king to any empty space
#move draw card to play pile
    # Move the top card from the drawn card to first playable pile
#move play piles around
    # Move any piles that can be placed on another one
    # move each pile only from the bottom card, and move only once per turn cycle
#draw next from deck
