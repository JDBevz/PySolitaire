#solitaire game logic
from cards import *

#initialize needed objects


#create 7 play piles, 4 set piles
#shuffle deck
#place cards into piles : index + 1 cards into pile, last card flipped up
playPiles = []

for i in range(7):
    playPiles.append(Pile())



#play order:
#move kings to empty :
    #Move any king to any empty space
#move draw card to play pile
    # Move the top card from the drawn card to first playable pile
#move play piles around
    # Move any piles that can be placed on another one
    # move each pile only from the bottom card, and move only once per turn cycle
#draw next from deck
