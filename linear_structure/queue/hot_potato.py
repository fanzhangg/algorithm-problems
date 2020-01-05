"""
Hot Potato:
- Pass an item from neighbor to neighbor as fast as they can.
- At a certain point in the game, the action is stopped & child who has the item
  is removed from the circle.
- Repeat until one child is left.

Problem:
- Input: a list of names and a constant `num` for counting.
- Output: the name of the last person remaining after repetitive counting by `num`

"""
import math
import time

import pandas as pd

from my_queue import Queue


def get_last(names: list, num: int) -> str:
    """
    :param names: a list of names
    :param num: the time of each time's passing
    :return: the name of the last person remaining after repetitive counting by `num`
    """
    # Use a queue to simulate the circle
    # Child holding the potato will be at the front of the queue
    circle_q = Queue()
    for name in names:
        circle_q.put(name)
    while True:
        # Stop the process when only one name remains
        if circle_q.size() == 1:
            break
        # When passing a potato, the simulation will simply dequeue and then immediately
        # enqueue the child, putting her at the end of the line
        for _ in range(num):
            front_child = circle_q.get()
            circle_q.put(front_child)
        # After passing potatoes `num` times, the child at the front will be removed permanently
        circle_q.get()
    return circle_q.get()


class Visualizer:
    def circle_q_to_str(self, names: list, potato_holder: str) -> str:
        height = math.floor(len(names) / 4) + 1
        width = math.ceil(len(names) / 4) + 1
        result = [[None] * width for _ in range(height)]
        names_iter = iter(names)

        for i in range(width):
            name = names_iter.__next__()
            if name == potato_holder:
                name = "[" + name + "]"
            result[0][i] = name

        for i in range(1, height - 1):
            name = names_iter.__next__()
            if name == potato_holder:
                name = "[" + name + "]"
            result[i][-1] = name

        for i in range(width - 1, -1, -1):
            try:
                name = names_iter.__next__()
            except StopIteration:
                break
            if name == potato_holder:
                name = "[" + name + "]"
            result[-1][i] = name

        for i in range(height - 1, 0, -1):
            try:
                name = names_iter.__next__()
            except StopIteration:
                break
            if name == potato_holder:
                name = "[" + name + "]"
            result[i][0] = name
        df = pd.DataFrame(result)
        return str(df)

    def print_animation(self, names: list, num: int):
        circle_q = Queue()
        for name in names:
            circle_q.put(name)
        while True:
            # Stop the process when only one name remains
            if circle_q.size() == 1:
                break
            # When passing a potato, the simulation will simply dequeue and then immediately
            # enqueue the child, putting her at the end of the line
            for i in range(num):
                front_child = circle_q.get()
                circle_q.put(front_child)
                print("Time:", i)
                print(self.circle_q_to_str(names, front_child))
                time.sleep(1)
            # After passing potatoes `num` times, the child at the front will be removed permanently
            name = circle_q.get()
            names.remove(name)
            print('\n')
        print("The last man:", circle_q.get())
