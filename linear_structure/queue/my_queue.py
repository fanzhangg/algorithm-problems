__name__ = ["Queue"]


class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, i):
        self.items.insert(0, i)

    def get(self):
        return self.items.pop()

    def empty(self):
        return self.items == []
