def selection_sort(items: list)->list:
    """
    Look for the largest name in a pass, and place it in a proper place after a pass.
    Repeat the process n-1 times.
    :param items: an unsorted list
    :return: an ordered list
    """
    for i in range(len(items) - 1):
        max_i = 0
        for j in range(1, len(items) - i):
            if items[j] > items[max_i]:
                max_i = j
        # Swap the last unsorted item and the max item
        items[max_i], items[len(items) - i - 1] = items[len(items) - i - 1], items[max_i]
    return items


def selection_sort_2(items: list)->list:
    for i in range(len(items) - 1, 0, -1):
        max_i = 0
        for j in range(1, i + 1):
            if items[j] > items[max_i]:
                max_i = j

        items[max_i], items[j] = items[j], items[max_i]
    return items
