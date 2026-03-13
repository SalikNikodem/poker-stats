from objects import Deck, Hand

if __name__ == '__main__':
    deck = Deck()
    deck.shuffleDeck()
    deck.printCards()

    hand1 = Hand("player1")
    hand1.printCards()
    hand1.take_card(deck)
    hand1.printCards()
    deck.printCards()