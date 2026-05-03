from hand_possibilities import is_pair, is_two_pair, is_flush, is_royal_flush, is_straight_flush, is_straight, is_high_card, is_full_house, is_three_of_a_kind, is_four_of_a_kind
from objects import Deck, Hand, Board

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
    deck = Deck.create_deck()
    board = Board(deck=deck)
    hands = Hand.deal_hands(num_of_players, deck, board)
    board.deal_cards()

    all_hands = []

    for hand in hands:
        all_hand = hand.all_cards()

        result, value, hand_name = evaluate_hand(all_hand)

        all_hands.append({
            'player': hand.player,
            'power': value,
            'best_5': result,
            'starting_hand': hand,
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

    winning_starting_hands = [w['starting_hand'] for w in winners]

    return all_hands, winners, hands, winning_starting_hands