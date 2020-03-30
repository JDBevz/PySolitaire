import cmd, sys
import os
from test import *

class SolitaireCmdShell(cmd.Cmd):
    intro = 'Solitaire!'
    prompt = '\n(prompt) '

    def postloop(self):
        pass
    def preloop(self):
        printPlay(playPiles, suitPiles, deck)
    #def precmd(self, line):
    #    os.system('cls')
    #    printPlay(playPiles, suitPiles, deck)
    #    return cmd.Cmd.precmd(self,line)
    def postcmd(self, stop, line):
            #os.system('cls')
            printPlay(playPiles, suitPiles, deck)
            return cmd.Cmd.postcmd(self,stop,line)


    #--Commands--#

    def do_move(self, arg):
        'Move cards from location a to location b. MOVE A B.\nMoves entire playable stack from A.'
        args = arg.split()
        a = b = None

        if len(args) == 2:
            try:
                #set first move arg
                if(args[0] == 'd'):
                    a = deck
                elif(args[0].isnumeric() and '0' < args[0] <='7'):
                    a = playPiles[int(args[0])-1]

                #set second move arg
                if(args[1].isnumeric() and '0' < args[1] <='7'):
                    b = playPiles[int(args[1])-1]
                elif(args[1] in suits):
                    b = suitPiles[suits.index[args[1]]]
            except Exception as e:
                print('Error: ', str(e))
                #raise
        #handle move with index
        elif len(args) == 3:
            pass
        else:
            print('Invalid number of arguments')

        print('\nmove(', args[0], ',', args[1], ')')
        move(a,b)

    def do_draw(self, arg):
        deck.drawNext()
        pass

    def do_reset(self):
        pass

    def do_quit(self, arg):
        print("\n\nQuitting\n\n")
        return True

    def do_none(self,arg):
        pass

    def emptyline(arg):
        pass



if __name__ == '__main__':
    print('start test')

    playPiles = []
    suitPiles = []
    deck = Deck()
    deck.resetDeck()
    deck.shuffleDeck()

    for i in range(3):
        playPiles.append(PlayPile())

    for i in suits:
        suitPiles.append(SuitPile(i))

    for x in range(3):
        for y in range(3):
            playPiles[x].cards.append(deck.cards.pop())

    playPiles[0].cards.append(Card('10','D',True))
    playPiles[1].cards.append(Card('9','S',True))
    playPiles[2].cards.append(Card('A','H',True))


    SolitaireCmdShell().cmdloop()
