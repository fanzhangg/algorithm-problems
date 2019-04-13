from __future__ import annotations
import random


class Person(object):
    def __init__(self, is_good: bool, name: int or str):
        self.is_good = is_good
        self.name = name

    def __bool__(self):
        return self.is_good

    def __str__(self):
        if self.is_good:
            return ":".join((str(self.name), "Good"))
        else:
            return ":".join((str(self.name), "Bad"))

    def other_is_good(self, other: Person)->bool:
        """
        Check the identity of other person
        :return: true if the person is good, else return false
        """
        if self.is_good:
            # good person always tells the true
            return other.is_good
        else:
            # bad person will either tell the truth or lie
            return random.choice((True, False))


def find_single_good(people: list)-> Person:
    """
    A divide and conquer algorithm to find a single good person
    :return: a good person
    """
    if len(people) == 1:
        return people[0]

    # if there is odd number people, it is possible that len(even_people) = len(odd_people) + 1
    for i in range(len(people)//2):
        p1 = people[2 * i]
        p2 = people[2 * i + 1]
        if p1.other_is_good(p2) and p2.other_is_good(p1):
            # delete one of two people
            people[2 * i] = None
        else:
            # delete both
            people[2 * i] = None
            people[2 * i + 1] = None

    # Remove all None items in the list
    people = [i for i in people if i is not None]

    if len(people) == 1:
        return people[0]
    elif len(people) % 2 == 1:
        people = people[:-1]

    return find_single_good(people)


def identify_all_people(good: Person, people: list) -> list:
    result = []
    for p in people:
        if good.other_is_good(p):
            result.append(True)
        else:
            result.append(False)
    return result

