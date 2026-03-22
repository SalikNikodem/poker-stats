import itertools
import random
from functools import total_ordering
from abc import ABC, abstractmethod
from collections import Counter

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
        return f"Card(Rank({self._rank}) Suit({self._suit}))"

    def __hash__(self):
        return hash((self._rank, self._suit))

    def __getitem__(self, index):
        if index == 0:
            return self._rank
        elif index == 1:
            return self._suit

class CardList(ABC):
    def __init__(self, cards=None):
        self._card_list = []

        self.rank_counts = Counter()
        self.suit_counts = Counter()

    def __iter__(self):
        return iter(self._card_list)

    @abstractmethod
    def printCards(self):
        pass

    def get_card_list(self):
        return self._card_list

    def get_rank_counts_list(self):
        return self.rank_counts

    def get_suit_counts_list(self):
        return self.suit_counts

    def add_card(self, card):
        self._card_list.append(card)
        self.rank_counts[card[0]] += 1
        self.suit_counts[card[1]] += 1

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
@total_ordering
class Hand(CardList):
    def __init__(self, player=None, deck=None, board=None, cards = None):
        super().__init__()
        self.player = player
        self.deck = deck
        self.board = board

        if cards:
            for card in cards:
                self.add_card(card)
            self._card_list = sorted(self._card_list, reverse=True)

    def __contains__(self, item):
        if isinstance(item, str):
            return any(card._rank == item for card in self._card_list)

        return item in self._card_list


    def __gt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return self._card_list > other._card_list

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return self._card_list == other._card_list

    def __getitem__(self, index):
        return self._card_list[index]
    def printCards(self):
        print(f"==={self.player} HAND===")
        for card in self._card_list:
            print(f"{str(card):<7}", end='')
        print()

    def take_card(self):
        card =  self.deck.take_card()
        self._card_list.append(card)

        self.rank_counts[card[0]] += 1
        self.suit_counts[card[1]] += 1

    def all_cards(self):
            cards =  sorted(self.get_card_list() + self.board.get_card_list(),reverse=True)
            return Hand(player=self.player, cards=cards)


class Board(CardList):
    def __init__(self, deck):
        super().__init__()
        self.deck = deck

    def printCards(self):
        print(f"=====BOARD=====")
        for card in self._card_list:
            print(f"{str(card):<7}", end='')
        print()

#flop river_turn
    def flop(self):
        self.deck.burn()
        for i in range(3):
            card = self.deck.take_card()
            self._card_list.append(card)

            self.rank_counts[card[0]] += 1
            self.suit_counts[card[1]] += 1

    def river_and_turn(self):
        self.deck.burn()
        card = self.deck.take_card()
        self._card_list.append(card)

        self.rank_counts[card[0]] += 1
        self.suit_counts[card[1]] += 1




