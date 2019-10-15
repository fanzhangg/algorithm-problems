import sys


class GoldFinder:
    def __init__(self):
        self.start = None

    def parse_input(self):
        """
        Read the input, get the map, and the coordinate of the starting point
        :return: a matrix of the map
        """
        mat = []
        width, height = [int(i) for i in sys.stdin.readline().split()]
        for i in range(height):
            mat.append([])
            for j in range(width):
                grid = sys.stdin.read(1)
                mat[i].append(grid)
                if grid == "P":
                    self.start = (i, j)   # get the position of staring point
            sys.stdin.read(1)  # escape the '\n'
        return mat

    def search_golds(self, mat: [[]]):
        """
        Search how many golds the person can collect without getting into the danger
        :param mat:
        :return: the number of golds
        """
        golds = 0
        visited, stack = set(), [self.start]
        while stack:    # use bfs to visit every grid in the map
            vertex = stack.pop()
            x, y = vertex
            if vertex not in visited and not mat[x][y] == "#":
                # add the vertex if it has not been visited or not the wall
                visited.add(vertex)     # visit the vertex

                if mat[x][y] == "G":    # get a gold
                    golds += 1

                if not self.has_trap_neighbor(vertex, mat):
                    # If not the person is at danger state, he has no option but tracking back
                    neighbors = ({(x, y-1), (x, y+1), (x-1, y), (x+1, y)} - visited)    # push neighbors to the stack
                    stack.extend(neighbors)
        return golds

    def has_trap_neighbor(self, coord: (int, int), mat: [[]]):
        """
        Check if there is a trp adjacent to the coordinate
        :param coord:
        :param mat:
        :return: true if there is a trap neighbor, else false
        """
        x, y = coord
        for (i, j) in {(x, y-1), (x, y+1), (x-1, y), (x+1, y)}:
            if mat[i][j] == "T":
                return True
        return False


gf = GoldFinder()
mat = gf.parse_input()
golds = gf.search_golds(mat)
print(golds)
