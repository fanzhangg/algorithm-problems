"""
Input: n dishes, each dish gets 2 scores
* No 2 values are same, n is a power of 2
Output: lower median of the 2n values (n-largest value)
"""


def query(k: int, judge_l: list)->int:
    """
    :k: value specified to a judge
    :judge_l: a sorted list of judge's values from the largest to shortest
    :return: the k-th largest value in the values given by judges
    """
    return judge_l[k]


def get_median(l1: list, l2: list)->int:
    if len(l1) == len(l2) == 1:
        return min(l1[0], l2[0])
    elif len(l1) == 1 or len(l2) == 1:
        return get_median_of_three(l1, l2)
    mid1_i = (len(l1) - 1) // 2
    mid1 = l1[mid1_i]
    mid2_i = (len(l2) - 1) // 2
    mid2 = l2[mid2_i]

    if mid1 > mid2:
        # ignore values greater than max(mid1, mid2)
        # search left half of the list of max(mid1, mid2)

        # ignore values smaller than max(mid1, mid2)
        # search right half of the list of min(mid1, mid2)
        return get_median(l1[:mid1_i + 1], l2[mid2_i:])
    else:
        return get_median(l1[mid1_i:], l2[:mid2_i + 1])


def get_median_of_three(l1: list, l2: list)-> int:
    l1 = l1 + l2
    l1.sort()
    return l1[1]
