from unittest import TestCase
from cancel_max_wallop_games import cancel_max_wallop_games, Game
import csv


class TestCancelMaxWallopGames(TestCase):
    @staticmethod
    def get_games()->list:
        games = []
        with open("shortListOfGames.csv") as file:
            reader = csv.reader(file)
            line_num = 0
            for row in reader:
                if line_num == 0:
                    pass
                else:
                    opponent = row[1]
                    walloping = int(row[2])
                    games.append(Game(opponent, walloping))
                line_num += 1
        return games

    def test_k_eq_3(self):
        games = self.get_games()
        cancelled_games = cancel_max_wallop_games(games, 3)
        self.assertEqual((24, {'Bethel', 'St. Thomas', 'Gustavus'}), cancelled_games)

    def test_k_eq_2(self):
        games = self.get_games()
        cancelled_games = cancel_max_wallop_games(games, 2)
        self.assertEqual((19, {'Carleton', 'St. Thomas'}), cancelled_games)



