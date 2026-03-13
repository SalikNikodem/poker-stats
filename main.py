from objects import Deck, Hand, Board

if __name__ == '__main__':
    deck = Deck()
    deck.shuffleDeck()
    deck.printCards()

    board = Board(deck)
    board.flop()
    board.printCards()
    deck.printCards()
    board.river_and_turn()
    board.river_and_turn()
    deck.printCards()
    board.printCards()

    hand1 = Hand("player1", deck, board)

    hand1.take_card()
    hand1.take_card()
    hand1.printCards()
    deck.printCards()
    print(hand1.get_card_list())
    print(board.get_card_list())
    lista = hand1.get_card_list() + board.get_card_list()
    print(lista)