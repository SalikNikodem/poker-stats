import itertools
import random
from functools import total_ordering
from abc import ABC, abstractmethod

# Card object, total ordering used for sort() function mainly.
@total_ordering
class Card:
    Values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._value = self.Values[rank]

    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._value > other._value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._value == other._value

    def __str__(self):
        return f"({self._rank} {self._suit})"

    def __repr__(self):
        return f"Card(Rank({self._rank}), Suit({self._suit}))"

    def __hash__(self):
        return hash((self._rank, self._suit))

#Deck object that contains all 52 cards with different methods
class CardList(ABC):
    def __init__(self):
        self._card_list = []

    #printing backwards for better efficiency in pop()
    @abstractmethod
    def printCards(self):
        pass

class Deck(CardList):
    _ranks = [x for x in Card.Values]
    _suits = ['♠','♥','♣','♦']

    def __init__(self):
        super().__init__()
        combinations = itertools.product(Deck._suits, Deck._ranks)
        self._card_list = [Card(r, s) for s,r in combinations]

    def printCards(self):
        print("="*48 + "DECK" + "="*48)
        for i, card in enumerate(self._card_list[::-1]):
            if i % 13 == 0 and i != 0: print()
            print(f"{str(card):<7}", end='')
        print()

    def shuffleDeck(self):
        random.shuffle(self._card_list)

    def take_card(self):
        return self._card_list.pop()

    #burn method to simulate real game as best as possible
    def burn(self):
        self._card_list.pop()


#Hand object that calculates best hand when combined with board
class Hand(CardList):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def printCards(self):
        print(f"==={self.player} HAND===")
        for card in self._card_list:
            print(f"{str(card):<7}", end='')
        print()

    def take_card(self, deck):
        card_to_take = deck.take_card()
        self._card_list.append(card_to_take)
        return card_to_take






