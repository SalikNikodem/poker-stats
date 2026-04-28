from helpers_and_functions import game
from models import  HandManager
if __name__ == '__main__':
    num = int(input("How many games you want to play?: "))
    players = int(input("How many players?: "))
    hand_stats = HandManager()

    for _ in range(num):
        all_hands, winners = game(players)

        hand_stats.update_stats(all_hands, winners)

    hand_stats.save_to_json()