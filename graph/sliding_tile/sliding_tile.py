from copy import deepcopy
import random


class Board:
    """
    Represent the sliding tile board
    """
    def __init__(self, data=None, b_row=2, b_col=2):
        if not data:
            self.data = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        else:
            self.data = data
        self.b_row = b_row
        self.b_col = b_col

    def __str__(self):
        s = ""
        for row in self.data:
            s = s + str(row) + "\n"
        return s

    def up(self):
        if self.b_row == 2:
            return False
        elif self.b_row == 0:
            self.data[0][self.b_col] = self.data[1][self.b_col]
            self.data[1][self.b_col] = 0
            self.b_row = 1
        else:
            self.data[1][self.b_col] = self.data[2][self.b_col]
            self.data[2][self.b_col] = 0
            self.b_row = 2

        return True

    def down(self):
        if self.b_row == 0:
            return False
        elif self.b_row == 1:
            self.data[1][self.b_col] = self.data[0][self.b_col]
            self.data[0][self.b_col] = 0
            self.b_row = 0
        else:
            self.data[2][self.b_col] = self.data[1][self.b_col]
            self.data[1][self.b_col] = 0
            self.b_row = 1

        return True

    def left(self):
        if self.b_col == 0:
            self.data[self.b_row][0] = self.data[self.b_row][1]
            self.data[self.b_row][1] = 0
            self.b_col = 1
        elif self.b_col == 1:
            self.data[self.b_row][1] = self.data[self.b_row][2]
            self.data[self.b_row][2] = 0
            self.b_col = 2
        else:
            return False

        return True

    def right(self):
        if self.b_col == 0:
            return False
        elif self.b_col == 1:
            self.data[self.b_row][1] = self.data[self.b_row][0]
            self.data[self.b_row][0] = 0
            self.b_col = 0
        else:
            self.data[self.b_row][2] = self.data[self.b_row][1]
            self.data[self.b_row][1] = 0
            self.b_col = 1

        return True

    def is_win(self):
        """
        :return: True if the board matches a winning condition
        """
        return self.data == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def get_neighbors(board: Board):
    """
    :return: Neighbors of the current board such as they can be reached at 1 step
    """
    b1 = deepcopy(board)
    if b1.up():
        yield b1
    b2 = deepcopy(board)
    if b2.down():
        yield b2
    b3 = deepcopy(board)
    if b3.left():
        yield b3
    b4 = deepcopy(board)
    if b4.right():
        yield b4


def search_solution(start):
    """
    :param start: Board to represent the starting case
    :return: a tuple of the dictionary of the node and its parent, the winning case
    """
    q = []
    visited = set()
    parent = {}
    q.append(start)
    visited.add(start)

    while not len(q) == 0:
        curr = q.pop(0)
        if curr.is_win():
            return parent, curr
        for n in get_neighbors(curr):
            if n not in visited:
                visited.add(n)
                parent[n] = curr
                q.append(n)


def get_start_board(steps):
    """
    :param steps: the number of steps
    :return: A randomly generated board after steps
    """
    start = Board()

    for i in range(steps):
        method = random.choice((start.up, start.down, start.left, start.right))
        method()

    return start


def get_steps(parent, end):
    """
    Get the board of each step from start to end
    :param parent: the dictionary of the node and its parent
    :param end: the board of the winning case
    :return: the path from start to end
    """
    path = [end]

    while True:
        end = parent[end]
        path.insert(0, end)
        if end == start:
            break
    return path


if __name__ == "__main__":
    start = get_start_board(60)
    parent, end = search_solution(start)
    steps = get_steps(parent, end)
    for s in steps:
        print(s)
