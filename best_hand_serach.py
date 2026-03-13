import random

from objects import Deck, Hand, Board
from random import seed

random.seed(2)

poker_hands = ['High Card', 'Pair', 'Double Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House',
               'Four of a kind', 'Straight Flush', 'Royal Flush']

deck = Deck()
board = Board(deck)
hand = Hand("player", deck, board)

deck.shuffleDeck()
deck.printCards()
hand.take_card()
hand.take_card()
board.flop()
board.river_and_turn()
board.river_and_turn()
karty = hand.all_cards()
print(karty)
ranks = {}
suits = {}
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

a = board.get_suit_counts_list()
b = hand.get_suit_counts_list()
list = a+b
print(list)
new_list = [list[x] for x in list if list[x] == 2]
print(new_list)
#SORTOWANIE PRZED ZWROCENIEM????????????????