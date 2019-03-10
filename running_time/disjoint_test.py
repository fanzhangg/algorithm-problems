"""
:given: sets S_1, S_2, S_3..., each of which is a subset of {1,2,...,n}
:output: whether some pair of these sets is disjoint - has no elements in common
"""


def are_disjoint(s1: set, s2: set)->bool:
    """
    Determine if two sets are disjoint (has no elements in common)
    """
    for i in s1:
        for j in s2:
            if i == j:
                return False
    return True


def has_disjoint_set(*args)->bool:
    """
    Determine if some sets in a list of sets are disjoint
    :param args:
    :return:
    """
    for s1 in args:
        for s2 in args:
            if not s1 == s2:
                disjoint = are_disjoint(s1, s2)
                if not disjoint:
                    return False
    return True


s1 = {1, 2, 3}
s2 = {10, 11, 12}
s3 = {100, 101, 102}
print(are_disjoint(s1, s2))
