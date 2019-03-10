from unittest import TestCase
from match_to_min_max_height_diff import *


class TestMatch(TestCase):
    def test_match_to_min_max_height_diff(self):
        team1 = [Player(1, 6), Player(2, 4), Player(3, 9)]
        team2 = [Player(1, 8), Player(2, 7), Player(3, 3)]
        pairs = match_to_min_max_height_diff(team1, team2)
        self.assertEqual([4, 3], [p.height for p in pairs[0]])
        self.assertEqual([6, 7], [p.height for p in pairs[1]])
        self.assertEqual([9, 8], [p.height for p in pairs[2]])
