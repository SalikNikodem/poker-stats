from objects import Deck, Hand, Board, Card

def is_flush(hand):
    colors = hand.get_suit_counts_list()
    for suit, count in colors.items():
        if count >=5:
            flush_cards = [card for card in hand if card._suit == suit]
            return Hand(player=hand.player, cards=flush_cards[:5])
    return None

def is_pair(hand):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

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

        return Hand(player=hand.player,cards=final_cards, sort=False)

def is_two_pair(hand):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

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

        return Hand(player=hand.player, cards=final_cards, sort=False)
    return None

def is_three_of_a_kind(hand):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

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

        return Hand(player=hand.player, cards=final_cards, sort=False)
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

        return Hand(player=hand.player, cards=final_cards, sort=False)
    return None

def is_full_house(hand):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

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
        return Hand(player=hand.player, cards=t + p, sort=False)
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
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    ranks = hand.get_rank_counts_list()

    hand_u = hand_unique(hand)

    sorted_ranks = sorted(ranks.keys(), key=lambda r : rank_values[r], reverse=True)
    if 'A' in sorted_ranks: sorted_ranks.append('A')
    fives = [sorted_ranks[i:i+5] for i in range(len(sorted_ranks)-4)]
    for five in fives:
        if five[-1] == 'A':
            rank_values['A'] = 1
        sum = 0
        for i in range(4):
            sum += rank_values[five[i]] - rank_values[five[i+1]]
        if sum == 4:
            flag = (True if '5' in five and 'A' in five else False)
            if flag:
                hand_u.ace_in_low_straight()
            cards = [card for card in hand_u if card._rank in five]
            return Hand(player=hand.player, cards=cards, sort=False)
    return None

def is_straight_flush(hand):
    suit_counts = hand.get_suit_counts_list()
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush_suit = suit
            break
    if not flush_suit:
        return None

    flush_cards = [card for card in hand if card._suit == flush_suit]
    all_flush_cards_hand = Hand(cards=flush_cards)

    return is_straight(all_flush_cards_hand)

def is_royal_flush(hand):
    straight_flush = is_straight_flush(hand)

    if straight_flush:
        if 'A' and '10' in straight_flush:
            return straight_flush
    return None

def is_high_card(hand):
    return Hand(player=hand.player, cards=hand[:5])

def evaluate_hand(hand):
    hand_values = [
        (10, is_royal_flush, "Royal Flush"),
        (9, is_straight_flush, "Straight Flush"),
        (8, is_four_of_a_kind, "Four of a Kind"),
        (7, is_full_house, "Full House"),
        (6, is_flush, "Flush"),
        (5, is_straight, "Straight"),
        (4, is_three_of_a_kind, "Three of a Kind"),
        (3, is_two_pair, "Two Pair"),
        (2, is_pair, "Pair")
    ]
    for value, func, name in hand_values:
        result = func(hand)
        if result:
            return result, value, name

    return is_high_card(hand), 1, 'High Card'


def game(num_of_players):
    hands = []

    deck = Deck()
    board = Board(deck=deck)

    for i in range(num_of_players):
        hands.append(Hand(player=f'PLAYER{i+1}', deck=deck, board=board))

    deck.shuffleDeck()

    for i in range(2):
        for hand in hands:
            hand.take_card()
    board.flop()
    board.river_and_turn()
    board.river_and_turn()

    all_hands = []

    for hand in hands:
        all_hand = hand.all_cards()

        result, value, hand_name = evaluate_hand(all_hand)

        all_hands.append({
            'player': hand.player,
            'power': value,
            'best_5': result,
            'name': hand_name
        })


    max_power = max(s['power'] for s in all_hands)

    contenders = [s for s in all_hands if s['power'] == max_power]

    winners = []

    if len(contenders) == 1:
        winners.append(contenders[0])
    else:
        current_best = contenders[0]
        winners = [current_best]

        for i in range(1,len(contenders)):
            challenger = contenders[i]

            if challenger['best_5'] > current_best['best_5']:
                current_best = challenger
                winners = [challenger]
            elif challenger['best_5'] == current_best['best_5']:
                winners.append(challenger)

    return all_hands, winners

import json
from pathlib import Path

class HandManager:
    def __init__(self, filename="stats/hand_stats.json"):

        self.file_path = Path(__file__).resolve().parent / filename
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.stats = self._load_stats()

    def _load_stats(self):
        if not self.file_path.exists():
            return {}

        try:
            with open(self.file_path, 'r', encoding="utf-8") as ff:
                return json.load(ff)
        except (json.JSONDecodeError, Exception):
            return {}

    def update_stats(self, all_hands, winners):
        num_winners = len(winners)
        win_value = 1.0 / num_winners

        for res in all_hands:
            name = res['name']
            if name not in self.stats:
                self.stats[name] = {"occurrences": 0, "wins": 0.0, "splits": 0}

            self.stats[name]["occurrences"] += 1

        for w in winners:
            name = w['name']
            self.stats[name]['wins'] += win_value
            if num_winners > 1:
                self.stats[name]["splits"] += 1

    def save_to_json(self):
        with open(self.file_path, 'w', encoding='utf-8') as ff:
            json.dump(self.stats, ff, indent=4, ensure_ascii=False)


hand_stats = HandManager()

for _ in range(100000):
    all_hands, winners = game(4)

    hand_stats.update_stats(all_hands, winners)

hand_stats.save_to_json()