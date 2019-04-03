"""
# Shell sort
- Break the original list into a number of smaller sublists, each of which is sorted
using an insertion sort;
- Use an increment `i` to create a sublist by choosing all items that are `i` items apart
"""


def shell_sort(items: list):
    sublist_count = len(items) // 2
    while sublist_count > 0:
        for start_i in range(sublist_count):
            gap_insertion_sort(items, start_i, sublist_count)
        sublist_count = sublist_count // 2


def gap_insertion_sort(items: list, start, gap):
    for i in range(start + gap, len(items), gap):
        current_value = items[i]
        position = i
        while position >= gap and items[position - gap] > current_value:
            items[position] = items[position - gap]
            position = position - gap

        items[position] = current_value
