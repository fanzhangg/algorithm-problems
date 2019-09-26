"""
Merge sort:
- recursively split a list in half
- if the list is empty or has one item, it is sorted by definition
- once the two halves are sorted, perform merge(
  * take two smaller sorted lists & combine them into a single, sorted, new list

:ref: https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
"""


def split(items: list)->tuple:
    """
    Split a list in half
    :return left and right lists
    """
    mid = len(items) // 2
    return items[:mid], items[mid:]


def merge(left_l: list, right_l: list)->list:
    """
    Merge two sorted lists into a single list
    :param left_l: a sorted list of the left half
    :param right_l: a sorted list of the right half
    :return: a sorted list merging the left and right lists
    """
    # Return another input list if one input list is empty
    if len(left_l) == 0:
        return right_l
    elif len(right_l) == 0:
        return left_l

    left_i = right_i = 0
    merged_l = []

    while len(merged_l) < len(left_l) + len(right_l):
        # Add the smaller name to the list and update the corresponding index
        if left_l[left_i] <= right_l[right_i]:
            merged_l.append(left_l[left_i])
            left_i += 1
        else:
            merged_l.append(right_l[right_i])
            right_i += 1

        # Reach the end of left list
        if left_i == len(left_l):
            # Append the reminder of the right list
            merged_l.extend(right_l[right_i:])
            break
        elif right_i == len(right_l):
            # Append the reminder of the left list
            merged_l.extend(left_l[left_i:])
            break
    return merged_l


def merge_sort(items: list)->list:
    if len(items) <= 1:
        return items
    else:
        left, right = split(items)

        return merge(merge_sort(left), merge_sort(right))

