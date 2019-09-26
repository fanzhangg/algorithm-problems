def bubble_sort(items: list)->list:
    """
    Makes multiple passes through a list. In each pass, it compares adjacent items and
    exchanges those that are out of order, and place the next largest name in its proper
    place
    :param items: a list of items
    :return: a sorted list
    """
    for i in range(len(items)-1):
        # since in i iteration, there are i items in the end sorted,
        # we only need to compare (len(items) - i) items
        for j in range(len(items) - i - 1):
            # swap two adjacent items if they are out of order
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def bubble_sort_2(items: list)->list:
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

