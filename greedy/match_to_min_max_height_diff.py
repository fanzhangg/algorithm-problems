from typing import List
from typing import Tuple


class Player:
    def __init__(self, index: int, height: int):
        self.index = index
        self.height = height

    def __lt__(self, other):
        return self.height < other.height

    def __str__(self):
        return "".join(("Player ", str(self.index), ": ", str(self.height)))


def match_to_min_max_height_diff(team1: List[Player], team2: List[Player])->List[Tuple[Player, Player]]:
    team1.sort()
    team2.sort()

    pairs = []
    for i in range(len(team1)):
        pair = (team1[i], team2[i])
        pairs.append(pair)
    return pairs
