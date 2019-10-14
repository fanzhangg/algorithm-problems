import sys


class WeakVerticesChecker:
    def __init__(self):
        self.vet_num = 0
        self.adj_list = dict()

    def parse_input(self, vet_num: int):
        self.adj_list = dict()
        for i in range(vet_num):
            line = sys.stdin.readline()
            neighbors = [int(i) for i in line.split()]
            self.update_adj_list(neighbors, i)

    def update_adj_list(self, mat_row: [int], cur_vet: int):
        cur_neighbor = 0
        neighbors = set()
        for value in mat_row:
            if value == 1:  # It is a neighbor
                neighbors.add(cur_neighbor)
            cur_neighbor += 1
        self.adj_list.update({cur_vet: neighbors})

    def get_weak_vertices(self):
        """
        :return: an ordered list of weak vertices
        """
        strong_vertices = set()
        for i in self.adj_list.keys():
            if i not in strong_vertices:    # skip checking if we already know it is a string vertex
                children = self.adj_list.get(i)
                for j in children:
                    grand_children = self.adj_list.get(j)
                    for k in grand_children:
                        if i in self.adj_list.get(k):
                            # check if there is a descendent in the 3rd level == the starting note
                            strong_vertices.add(i)
                            break
        weak_set = set(self.adj_list.keys()) - strong_vertices
        weak_list = list(weak_set)
        weak_list.sort()
        return weak_list


if __name__ == "__main__":
    checker = WeakVerticesChecker()
    while True:
        vert_num = int(sys.stdin.readline())
        if vert_num == -1:
            break
        checker.parse_input(vert_num)
        weak_vertices = checker.get_weak_vertices()
        print(" ".join([str(i) for i in weak_vertices]))

