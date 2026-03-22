import random
from objects import Deck, Hand, Board, Card

random.seed(2)

poker_hands = ['High Card', 'Pair', 'Double Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House',
               'Four of a kind', 'Straight Flush', 'Royal Flush']

deck = Deck()
board = Board(deck)
hand1 = Hand("player1", deck, board)
hand2 = Hand("player2", deck, board)
deck.shuffleDeck()
hand1.take_card()
hand1.take_card()
hand2.take_card()
hand2.take_card()
board.flop()
board.river_and_turn()
board.river_and_turn()
karty1 = hand1.all_cards()
karty2 = hand2.all_cards()

# _suits = ['♠', '♥', '♣', '♦']
reka_ustawiona = Hand(cards=[
Card("5", '♠'),
Card("K", '♠'),
Card("A", '♠'),
Card("K", '♠'),
Card("Q", '♠'),
Card("Q", '♠'),
Card("5", '♠')])
reka_ustawiona2 = Hand(cards=[
Card("Q", '♠'),
Card("J", '♠'),
Card("8", '♠'),
Card("5", '♠'),
Card("2", '♠'),
Card("10", '♠'),
Card("10", '♠')])

rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def is_flush(hand):
    colors = hand.get_suit_counts_list()
    for suit, count in colors.items():
        if count >=5:
            flush_cards = [card for card in hand if card._suit == suit]
            return Hand(player=hand.player, cards=flush_cards[:5])
    return None

def is_pair(hand):
    ranks = hand.get_rank_counts_list()
    sorted_ranks = sorted(ranks.keys(), key=lambda r: rank_values[r], reverse=True)

    rank = None
    for k in sorted_ranks:
        if ranks[k] == 2:
            rank = k
            break

    if rank:
        cards = [card for card in hand if card._rank == rank]
        rest = [card for card in hand if card._rank != rank]

        final_cards = cards + rest[:3]

        return Hand(player=hand.player,cards=final_cards)


def is_two_pair(hand):
    ranks = hand.get_rank_counts_list()
    pairs = []

    for k,v in ranks.items():
        if v == 2:
            pairs.append(k)

    if len(pairs) >= 2:
        pairs = sorted(pairs, key=lambda r: rank_values[r], reverse=True)[:2]

        rank1, rank2 = pairs[0], pairs[1]

        cards1 = [card for card in hand if card._rank == rank1][:2]
        cards2 = [card for card in hand if card._rank == rank2][:2]

        rest = [card for card in hand if card._rank != rank1 and card._rank != rank2]

        final_cards = cards1 + cards2 + rest[:1]

        return Hand(player=hand.player, cards=final_cards)
    return None

# 2 times 3 is full house, but we don't care since we are going to evaluate from the highest possible hand
def is_three_of_a_kind(hand):
    ranks = hand.get_rank_counts_list()
    rank = None
    sorted_ranks = sorted(ranks.keys(), key=lambda r: rank_values[r], reverse=True)

    for k in sorted_ranks:
        v = ranks[k]
        if v == 3:
            rank = k
            break
    if rank:
        cards = [card for card in hand if card._rank == rank]
        rest = [card for card in hand if card._rank != rank]

        final_cards = cards + rest[:2]

        return Hand(player=hand.player, cards=final_cards)
    return None

def is_four_of_a_kind(hand):
    ranks = hand.get_rank_counts_list()
    rank = None
    for k,v in ranks.items():
        if v == 4:
            rank = k
            break
    if rank:
        cards = [card for card in hand if card._rank == rank]
        rest = [card for card in hand if card._rank != rank]

        final_cards = cards + rest[:1]

        return Hand(player=hand.player, cards=final_cards)
    return None

x = is_two_pair(reka_ustawiona)
x.printCards()
