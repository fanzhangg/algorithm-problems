import random
import math

"""
Suppose you are given a budget of k = 2 jars. 
Describe a strategy for finding the highest safe rung that requires you to drop a jar at most f(n) times, 
for some function f(n) that grows slower than linearly. 
"""


def get_random_rungs(length: int)->list:
    """
    Get a rungs whose size is `length`
    :param length: the length of rungs
    :return: a list represents rungs (True if the jar will break when dropped from the rung, False if it will not
    """
    highest_safe_rung = random.randint(0, length-1)
    print("expected highest safe rung:", highest_safe_rung)
    return [False] * (highest_safe_rung + 1) + [True] * (length - highest_safe_rung - 1)


def find_highest_safe_rung(l: list)->int:
    """
    Find the highest safe rung
    :param l: a list represents rungs
    :return: the index of the highest safe rung
    """
    h = math.ceil(math.sqrt(len(l)))
    curr_h = h - 1
    while not l[curr_h]:
        if len(l) - 1 - curr_h <= h:
            # test the highest rung
            h = len(l) - 1 - curr_h
            curr_h = len(l) - 1
        else:
            curr_h += h
    for x in range(curr_h-h+1, curr_h + 1):
        if l[x]:
            return x - 1


if __name__ == "__main__":
    rungs = get_random_rungs(10)
    print("rungs:", rungs)
    print("size:", len(rungs))
    actual_highest_safe_rung = find_highest_safe_rung(rungs)
    print("actual highest safe rung", actual_highest_safe_rung)
