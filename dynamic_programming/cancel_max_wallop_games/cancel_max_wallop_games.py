from typing import List, Tuple


class Game(object):
    def __init__(self, opponent: str, walloping: int):
        self.opponent = opponent
        self.walloping = walloping

    def __str__(self):
        return ":".join((self.opponent, str(self.walloping)))


def cancel_max_wallop_games(games: List[Game], max_games_num: int)->Tuple[int, List[str]]:
    """
    :games: sorted list of wallopings of n games [v1, v2, ..., vn]
    :max_games_num: the max number of games that can be cancelled
    :return: a set S of games you can cancel: |S| <= k, no 2 adjacent games are in S, and the sum of v in S is maximized

    Recurrence relationship:
    - if i = 0, OPT(i, k) = 0
    - if k = 0, OPT(i, k) = 0
    - if i = 1, and k != 0, OPT(i, k) = vi
    - else, OPT(i, k) = max(OPT(i-1, k), OPT(i-2, k - 1) + vi)
    """
    cancelled_games = [[None for _ in range(max_games_num + 1)] for _ in range(len(games) + 1)]
    # create a matrix: [cancelled games' size[max cancelled games]]
    opt = [[None for _ in range(max_games_num + 1)] for _ in range(len(games) + 1)]

    # when there is 0 item, all opt = 0
    for k in range(max_games_num + 1):
        opt[0][k] = 0
        cancelled_games[0][k] = set()

    # when the max cancelled game is 0, all opt = 0
    for i in range(len(games) + 1):
        opt[i][0] = 0
        cancelled_games[i][0] = set()

    # when there is 1 item i, and k != 0, we can only choose the item, and otp = vi
    for k in range(1, max_games_num + 1):
        opt[1][k] = games[0].walloping
        cancelled_games[1][k] = {games[0].opponent}

    for k in range(1, max_games_num + 1):
        for i in range(2, len(games) + 1):
            if opt[i-1][k] >= games[i - 1].walloping + opt[i - 2][k - 1]:
                opt[i][k] = opt[i-1][k]
                cancelled_games[i][k] = cancelled_games[i-1][k]
            else:
                opt[i][k] = games[i - 1].walloping + opt[i - 2][k - 1]
                # Add games[i-1] to the set
                cancelled_game_set = cancelled_games[i - 2][k - 1]
                cancelled_game_set.add(games[i - 1].opponent)
                cancelled_games[i][k] = cancelled_game_set
    return opt[-1][-1], cancelled_games[-1][-1]
