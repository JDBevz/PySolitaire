#Solitaire testing
from cards import *

cardTest = Card('D', 1)
print(cardTest)
y = Pile()

for x in values:
    y.addCard(Card('S',x))

y.printPile()

set1 = {1,2,3,4,5,6}

for x in set1:
    print(x)
