from visualizer import *

"""
The bubble sort algorithm sorts an unordered list by repeatedly stepping through the list and swapping items if they are
in the wrong order (item bigger than the next one)
"""


def sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                # swap l[j] and l[j+1]
                l[j], l[j + 1] = l[j + 1], l[j]
                display(l, j, j + 1)
                display_match(l, True, j, j + 1)
            else:
                display_match(l, False, j, j + 1)
    return l


random_l = create_random_list(10)

sorted_l = sort(random_l)

display_end(sorted_l)

print(sorted_l)
