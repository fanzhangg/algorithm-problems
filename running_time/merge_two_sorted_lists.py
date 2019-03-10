"""
    :given: we are given two lists of n numbers arranged in ascending order.
    :output: merge these into a single list c1, c2, . . . , c2n that is also arranged in ascending order.
    :example: Merging the lists 2, 3, 11, 19 and 4, 9, 16, 25 results in the output 2, 3, 4, 9, 11, 16, 19, 25.
"""

def merge_two_sorted_lists(l1: list, l2: list)->list:
    l1 = iter(l1)
    l2 = iter(l2)
    new_l = []
    cur1 = next(l1)
    cur2 = next(l2)
    while True:
        if cur1 <= cur2:
            new_l.append(cur1)
            try:
                cur1 = next(l1)
            except StopIteration:
                cur1 = None
                break
        else:
            new_l.append(cur2)
            try:
                cur2 = next(l2)
            except StopIteration:
                cur2 = None
                break

    # once one list is empty, append the rest of another list to the output
    if cur1:
        while True:
                new_l.append(cur1)
                try:
                    cur1 = next(l1)
                except StopIteration:
                    break
    else:
        while True:
            new_l.append(cur2)
            try:
                cur2 = next(l2)
            except StopIteration:
                break
    return new_l


if __name__=="__main__":
    l1 = [1, 3, 4, 5, 8]
    l2 = [3, 4, 4, 7]
    merged_l = merge_two_sorted_lists(l1, l2)
    print("2.", merged_l)