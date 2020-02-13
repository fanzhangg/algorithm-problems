class GameEntry:
    """Represent one entry of a list of high scores"""
    def __init__(self, name: str, score: int):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"{self._name}: {self._score}"


class Scoreboard:
    """Fixed-length sequence of high scores in non-decreasing order"""
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k: int):
        """
        :param k: index
        :return: the entry at k
        """
        return self._board[k]

    def __str__(self):
        """
        :return: string representation of the high score list
        """
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry: GameEntry):
        """
        :param entry: a game entry
        :return: Adding entry to high scores
        """
        score = entry.get_score()

        if self._n < len(self._board) or score > self._board[-1].get_score():
            # Check if the entry qualifies as a high score
            if self._n < len(self._board):  # No need to discard old score
                self._n += 1

            j = self._n - 1
            while True:
                if j <= 0:
                    break
                if self._board[j - 1].get_score() > score:  # The previous score is greater
                    break
                self._board[j] = self._board[j-1]    # Shift entry from j-1 to j
                j -= 1  # Decrease j
            self._board[j] = entry


sb = Scoreboard()
for x in range(20, 1, -1):
    entr = GameEntry("nub", x)
    sb.add(entr)
print(sb)
