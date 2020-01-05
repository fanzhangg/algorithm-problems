class Stack(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, i):
        self.items.append(i)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items == []

    def __iter__(self):
        return iter(self.items)
