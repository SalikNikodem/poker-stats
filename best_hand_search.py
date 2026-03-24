from objects import Deck, Hand, Board, Card

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
Card("4", '♠'),
Card("A", '♠'),
Card("10", '♠'),
Card("J", '♠'),
Card("Q", '♠'),
Card("K", '♠')])
reka_ustawiona2 = Hand(cards=[
Card("Q", '♠'),
Card("5", '♠'),
Card("4", '♠'),
Card("3", '♠'),
Card("2", '♠'),
Card("6", '♠'),
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

def is_full_house(hand):
    ranks = hand.get_rank_counts_list()

    sorted_ranks = sorted(ranks.keys(), key=lambda r : rank_values[r], reverse=True)

    trip_rank = None
    pair_rank = None

    for rank in sorted_ranks:
        if ranks[rank] >= 3:
            trip_rank = rank
            break

    if trip_rank:
        for rank in sorted_ranks:
            if ranks[rank] >=2 and rank != trip_rank:
                pair_rank = rank
                break

    if trip_rank and pair_rank:

        t = [card for card in hand if card._rank == trip_rank][:3]
        p = [card for card in hand if card._rank == pair_rank][:2]
        return Hand(player=hand.player, cards=t + p)
    return None
def hand_unique(hand):
    h = []
    ranks = []
    for card in hand:
        if card._rank not in ranks:
            ranks.append(card._rank)
            h.append(card)

    return Hand(cards=h,sort=False)
def is_straight(hand):
    rv = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    ranks = hand.get_rank_counts_list()

    hand_u = hand_unique(hand)

    sorted_ranks = sorted(ranks.keys(), key=lambda r : rank_values[r], reverse=True)
    if 'A' in sorted_ranks: sorted_ranks.append('A')
    fives = [sorted_ranks[i:i+5] for i in range(len(sorted_ranks)-4)]
    for five in fives:
        if five[-1] == 'A':
            rv['A'] = 1
        sum = 0
        for i in range(4):
            sum += rv[five[i]] - rv[five[i+1]]
        if sum == 4:
            flag = (True if '5' in five and 'A' in five else False)
            if flag:
                hand_u.ace_in_low_straight()
            cards = [card for card in hand_u if card._rank in five]
            return Hand(player=hand.player, cards=cards, sort=False)
    return None


def is_straight_flush(hand):
    flush = is_flush(hand)
    if flush:
        straight = is_straight(flush)
        if straight:
            return straight
    return None

def is_royal_flush(hand):
    straight_flush = is_straight_flush(hand)

    if straight_flush:
        if 'A' and '10' in straight_flush:
            return straight_flush
    return None

def is_high_card(hand):
    return Hand(player=hand.player, cards=hand[:5])

