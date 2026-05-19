from helpers_and_functions import game
from models import  HandManager

MIN_PLAYERS = 2
MAX_PLAYERS = 10

if __name__ == '__main__':
    try:
        num_input = input("How many games you want to play?: ")
        players_input = input("How many players?: ")

        num = int(num_input)
        players = int(players_input)

        if players < MIN_PLAYERS: raise ValueError(f"Error: Please provide value bigger than {players}.")
        elif players > MAX_PLAYERS: raise ValueError(f"Error: Please provide less than {players} players.")

        hand_stats = HandManager()

        step = max(1, num // 100)
        for i in range(num):

            all_hands, winners, hands, winning_starting_hands = game(players)

            hand_stats.update_stats(all_hands, winners)

            if (i + 1) % step == 0:
                current_percent = (i + 1) // step
                bars = current_percent // 10
                spaces = 10 - bars

                print(f"IN PROGRESS {'|' * bars}{' ' * spaces} {current_percent}%")

        hand_stats.save_to_json()
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Error: Please provide valid whole number.")
        else:
            print(f"Error : {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}.")


#sprawdzic czy da sie gdzie zmeirzyc ile co sie robi