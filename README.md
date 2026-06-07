# poker-stats
Python program that calculates % for specific poker hand 

Python program that uses calculation functions and objects to simulate real poker game for any number of players.

Features

-Full implementation of Texas Hold'em rules and hand rankings.
-Precise kicker evaluation to properly handle split pots.
-Automatically creates, loads, and updates a local JSON database so your simulation data accumulates over multiple runs.
-A text-based, optimized progress bar in the terminal to track long-running simulations.
-Built entirely using Python's standard library (`collections`, `itertools`, `pathlib`)

As of right now, program allows to simulate poker game any amount of times and saves results in json file.

Example of json:
{
    "Pair": {
        "occurrences": 178793,
        "wins": 24484.99999999996,
        "splits": 2411
    },
    "Three of a Kind": {
        "occurrences": 20058,
		...
  

Installation

git clone https://github.com/SalikNikodem/poker-stats.git

Project Structure:
-'main.py' - main program, use it in terminal
-'objects.py' - all Card, Deck, Hand, Board classes for use
-'hand_possibillities.py' - all poker hand possibillities using Card and Hand classes
-'helpers_and_functions.py' - functions used for for 'main.py' and evaluating hands
-'models.py' - HandManager model used for file tracking

Terminal preview

How many games you want to play?: 1000
How many players?: 4
Starting simulation...
IN PROGRESS [||        ] 20%
IN PROGRESS [|||||     ] 50%
IN PROGRESS [||||||||||] 100%
Simulation finished successfully! Stats saved.

