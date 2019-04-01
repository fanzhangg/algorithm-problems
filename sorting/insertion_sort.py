def insertion_sort(items: list)->list:
    """
    Maintain a sorted sublist in the lower positions of the list
    :param items:
    :return:
    """
    for i in range(len(items)):
        min_i = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_i]:
                min_i = j
        # swap the first unsorted item with the min item
        items[min_i], items[i] = items[i], items[min_i]
    return items
