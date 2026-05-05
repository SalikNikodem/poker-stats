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

        for name in self.stats:
            occ = self.stats[name]["occurrences"]
            wins = self.stats[name]["wins"]
            self.stats[name]["win_rate"] = f"{(wins / occ * 100):.2f}%" if occ > 0 else "0%"

    def save_to_json(self):
        with open(self.file_path, 'w', encoding='utf-8') as ff:
            json.dump(self.stats, ff, indent=4, ensure_ascii=False)
