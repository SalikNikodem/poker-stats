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
Card("4", '♠'),
Card("4", '♠'),
Card("4", '♠'),
Card("5", '♠'),
Card("A", '♠')])
reka_ustawiona.printCards()
reka_ustawiona2 = Hand(cards=[
Card("4", '♠'),
Card("4", '♠'),
Card("5", '♠'),
Card("5", '♠'),
Card("4", '♠')])
reka_ustawiona2.printCards()



def flush(hand):
    colors = hand.get_suit_counts_list()
    for suit, count in colors.items():
        if count >=5:
            flush_cards = [card for card in hand if card._suit == suit]
            return Hand(player=None, cards=flush_cards)
    return None

x = flush(reka_ustawiona)
x.printCards()

print(reka_ustawiona < reka_ustawiona2)

