# poker-stats
Python program that calculates % for specific poker hand 

Python program that uses calculation functions and objects to simulate real poker game for any number of players.

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
  
While program is running, there is a progress bar that allows user to see current percent of games played.
It is helpful to calculate amount of time needed and operations done in time.


Installation

git clone https://github.com/SalikNikodem/poker-stats.git

Project Structure:
-'main.py' - main program, use it in terminal
-'objects.py' - all Card, Deck, Hand, Board classes for use
-'hand_possibillities.py' - all poker hand possibillities using Card and Hand classes
-'helpers_and_functions.py' - functions used for for 'main.py' and evaluating hands
-'models.py' - HandManager model used for file tracking